import os
import sys  # Import the sys module to use sys.exit
import pandas as pd
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

# --- Configuration ---
# Create a Flask application instance
app = Flask(__name__)
# Enable CORS for all routes, allowing your frontend to talk to the API
CORS(app)
# Define the path to the folder containing chapter CSV files
DATA_FOLDER = os.path.join(os.path.dirname(__file__), 'data')

# --- Helper Functions (Identical to before) ---

def get_available_chapters():
    """Scans the data directory and returns a list of available chapter names."""
    # This function is already designed to handle a missing directory gracefully
    # by returning an empty list, which we will check at startup.
    try:
        files = os.listdir(DATA_FOLDER)
        # Filter for non-empty CSV files only
        chapters = []
        for f in files:
            if f.endswith('.csv'):
                try:
                    if os.path.getsize(os.path.join(DATA_FOLDER, f)) > 0:
                        chapters.append(os.path.splitext(f)[0])
                except OSError:
                    continue # Ignore files that can't be accessed
        return sorted(chapters)
    except FileNotFoundError:
        return []

def load_questions_from_chapters(chapter_list):
    """Loads questions from a given list of chapter CSV files into a single pandas DataFrame."""
    all_dfs = []
    for chapter_name in chapter_list:
        file_path = os.path.join(DATA_FOLDER, f"{chapter_name}.csv")
        if os.path.exists(file_path):
            try:
                df = pd.read_csv(file_path)
                if not df.empty:
                    all_dfs.append(df)
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
                continue
    
    if not all_dfs:
        return pd.DataFrame() # Return an empty DataFrame instead of None

    return pd.concat(all_dfs, ignore_index=True)


# --- API Endpoints ---

@app.route('/', methods=['GET'])
def home():
    """
    Serves the main index.html file as the homepage.
    Flask will automatically look for this file in the 'templates' folder.
    """
    return render_template('index.html')

@app.route('/chapters', methods=['GET'])
def list_chapters():
    """Endpoint to list all available chapters."""
    chapters = get_available_chapters()
    # This check is now redundant because of the startup check, but good for safety
    if not chapters:
        return jsonify({"error": "No chapter data found. The 'data' directory on the server is likely empty."}), 404
    return jsonify({"chapters": chapters})


@app.route('/quiz', methods=['GET'])
def create_quiz():
    """Generates a quiz based on query parameters."""
    chapters_str = request.args.get('chapters')
    if not chapters_str:
        return jsonify({
            "error": "The 'chapters' query parameter is required.",
            "usage": "/quiz?chapters=Chapter_01&count=20"
        }), 400
    
    selected_chapters = [ch.strip() for ch in chapters_str.split(',')]
    
    try:
        count = int(request.args.get('count', 10))
        if not (10 <= count <= 100):
            raise ValueError()
    except (ValueError, TypeError):
        return jsonify({"error": "The 'count' parameter must be an integer between 10 and 100."}), 400

    all_questions_df = load_questions_from_chapters(selected_chapters)

    # UPDATED: Check for an empty DataFrame correctly.
    if all_questions_df.empty:
        return jsonify({"error": f"No questions found for the specified chapters: {', '.join(selected_chapters)}"}), 404

    num_available = len(all_questions_df)
    if num_available < count:
        quiz_df = all_questions_df.copy()
        message = f"Warning: Requested {count} questions, but only {num_available} were available."
    else:
        quiz_df = all_questions_df.sample(n=count)
        message = f"Successfully generated a quiz with {count} questions."

    quiz_questions = []
    for index, row in quiz_df.iterrows():
        question_data = {
            "id": int(row['sl']),
            "question": row['question'],
            "options": {
                "opt_1": row['opt_1'],
                "opt_2": row['opt_2'],
                "opt_3": row['opt_3'],
                "opt_4": row['opt_4']
            },
            "answer": row['answer'] 
        }
        quiz_questions.append(question_data)

    response = {
        "quiz_title": f"Quiz from: {', '.join(selected_chapters)}",
        "message": message,
        "question_count": len(quiz_questions),
        "questions": quiz_questions
    }
    
    return jsonify(response)


# --- Main execution block (UPDATED) ---
if __name__ == '__main__':
    # Strict check for the data directory and its contents at startup
    if not get_available_chapters():
        print("---" * 20)
        print("FATAL ERROR: The 'data' directory is missing, empty, or contains no valid/non-empty CSV files.")
        print(f"Please create a 'data' folder in the same directory as '{__file__}' and add your chapter CSV files.")
        print("---" * 20)
        sys.exit(1) # Exit the script with an error code
    
    print("---" * 20)
    print("Found chapter data. Starting the Quiz Master server...")
    print("---" * 20)
    app.run(debug=True, port=5000)
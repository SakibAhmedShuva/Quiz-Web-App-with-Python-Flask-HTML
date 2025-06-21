# Quiz Web App with Python, Flask, and HTML

![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.x-black.svg)
![Frontend](https://img.shields.io/badge/Frontend-HTML_CSS_JS-orange.svg)

A sleek, modern, and interactive quiz platform built with a Python and Flask backend and a pure HTML, CSS, and JavaScript frontend. This application allows users to generate custom quizzes from a library of questions stored in CSV files.

![image](https://github.com/user-attachments/assets/89a90742-07b8-4908-aeff-c4c7b1c9de8c)


![image](https://github.com/user-attachments/assets/618245c8-db48-4a29-b169-fd51e2ee23f6)


![image](https://github.com/user-attachments/assets/9e6ba774-3e65-4c70-bbdd-6712d7c7bb4e)


*Note: Add a screenshot.png file to the root of your repository for the image above to display correctly.*

## ✨ Key Features

- **Dynamic Quiz Generation**: Select from available chapters and specify the number of questions to create a unique quiz every time.
- **Flexible Quiz Formats**: Choose between two modes:
  - **Paginated View**: Answer questions one by one with a progress bar.
  - **Single Page View**: View and answer all questions on a single scrollable page.
- **Modern UI/UX**: A clean, responsive, and intuitive interface designed for a great user experience.
- **Dark/Light Theme**: Toggle between dark and light modes, with the user's preference saved in their browser.
- **Instant Results & Review**: Get your score immediately after submission, complete with a visual score circle, detailed stats, and an option to review every question and its correct answer.
- **Data-Driven**: Questions are loaded dynamically from simple CSV files, making it incredibly easy to add or manage content without touching the code.
- **Zero Frontend Dependencies**: Built with pure vanilla JavaScript, HTML, and CSS for a lightweight and fast experience.

## 🛠️ Technology Stack

- **Backend**: Python, Flask, Pandas
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Development**: Flask-CORS

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8 or newer
- pip (Python package installer)

### Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/SakibAhmedShuva/Quiz-Web-App-with-Python-Flask-HTML.git
   cd Quiz-Web-App-with-Python-Flask-HTML
   ```

2. **Create and activate a virtual environment (recommended):**
   
   On macOS and Linux:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
   
   On Windows:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Install the required Python packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Verify your data:**
   Ensure the `data` directory exists and contains at least one non-empty `.csv` file with quiz questions. See the [Customization](#️-customization-adding-your-own-questions) section for the required format.

5. **Run the Flask application:**
   ```bash
   python app.py
   ```
   The server will start, and you will see output in your terminal indicating it's running.

6. **Access the application:**
   Open your web browser and navigate to: `http://127.0.0.1:5000`

## 📁 Project Structure

```
Quiz-Web-App-with-Python-Flask-HTML/
├── app.py                  # Main Flask backend logic and API endpoints
├── requirements.txt        # Python dependencies for pip
├── data/
│   └── Chapter_01.csv      # Example CSV file with quiz questions
│   └── ...                 # Add other chapter CSVs here
├── templates/
│   └── index.html          # The single HTML file containing all frontend code (HTML, CSS, JS)
└── README.md               # You are here!
```

## ⚙️ How It Works

1. **Backend Initialization**: When `app.py` is run, Flask starts a web server. The script performs a startup check to ensure the data directory exists and contains valid chapter files.

2. **Frontend Loading**: When a user visits the root URL (`/`), Flask serves the `index.html` file.

3. **Chapter Fetching**: The JavaScript in `index.html` immediately sends a request to the `/chapters` API endpoint. The backend scans the data directory and returns a JSON list of available chapter names.

4. **Quiz Configuration**: The user selects chapters, sets the number of questions, and chooses a quiz format on the UI.

5. **Quiz Generation**: Clicking "Generate Quiz" triggers a request to the `/quiz` endpoint with the user's selections as query parameters (e.g., `/quiz?chapters=Chapter_01,Chapter_02&count=15`).

6. **Data Processing**: The backend uses Pandas to read the selected CSV files, combines the questions, randomly samples the requested number of questions, and returns them as a JSON object.

7. **Quiz Display**: The frontend JavaScript receives the quiz data and dynamically builds the HTML for the quiz, either in paginated mode or single-page mode.

8. **Submission and Scoring**: After the user submits their answers, all logic for scoring, result display, and answer review is handled client-side by JavaScript.

## ✍️ Customization: Adding Your Own Questions

It's very easy to add your own chapters and questions.

### Steps:

1. **Create a CSV file**: Inside the `data` directory, create a new file with a `.csv` extension (e.g., `My_New_Chapter.csv`). The filename (without the extension) will be used as the chapter name in the UI.

2. **Format the CSV**: Your CSV file must have the following columns:
   - `sl`: A unique serial number or ID for the question
   - `question`: The text of the question
   - `opt_1`: The text for the first option
   - `opt_2`: The text for the second option
   - `opt_3`: The text for the third option
   - `opt_4`: The text for the fourth option
   - `answer`: The correct option's column name (e.g., `opt_1`, `opt_2`, `opt_3`, or `opt_4`)

### Example `My_New_Chapter.csv`:

```csv
sl,question,opt_1,opt_2,opt_3,opt_4,answer
1,"What is the capital of France?","London","Berlin","Paris","Madrid","opt_3"
2,"Which planet is known as the Red Planet?","Earth","Mars","Jupiter","Venus","opt_2"
```

3. **Restart the Server**: If the server is already running, restart it (`Ctrl+C` then `python app.py`) to let it detect the new chapter file. The new chapter will now appear as an option on the quiz setup page.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

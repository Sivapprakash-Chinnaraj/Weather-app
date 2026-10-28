🌤️ Weather Dashboard

A lightweight, full-stack weather web application built to practice API integration, backend database management, and collaborative Git workflows.

🚀 Features

Live Weather Data: Fetches real-time temperature and conditions using the OpenWeatherMap API.

Quick Select: Clickable default city chips (Coimbatore, Bengaluru, Chennai) for instant forecasts.

Search History: Automatically saves recent city searches to a local SQLite database and displays them on the dashboard.

🛠️ Tech Stack

Frontend: HTML5, CSS3, Vanilla JavaScript

Backend: Python (Flask)

Database: SQLite

Version Control: Git & GitHub

📂 Project Structure

weather-app/
├── app.py                 # Flask server and database logic
├── requirements.txt       # Python dependencies
├── .gitignore             # Ignored files (database, virtual environments)
├── README.md              # Project documentation
├── instance/
│   └── weather.db         # SQLite database (auto-generated)
├── static/
│   ├── css/
│   │   └── style.css      # Frontend styling
│   └── js/
│       └── script.js      # API fetching and DOM manipulation
└── templates/
    └── index.html         # Main dashboard layout


⚙️ Local Setup and Installation

Follow these steps to run the project on your local machine:

1. Clone the repository:

git clone https://github.com/YourUsername/weather-app.git
cd weather-app


2. Install dependencies:
It is recommended to use a virtual environment. Once activated, install Flask:

pip install -r requirements.txt


3. Add your API Key:

Create a free account at OpenWeatherMap.

Generate an API key.

Open static/js/script.js and replace 'YOUR_API_KEY' with your actual key. (Note: Never commit your real API key to GitHub!)

4. Run the application:

python app.py


The SQLite database (weather.db) will generate automatically.

Open your web browser and navigate to http://127.0.0.1:5000/.

🤝 Contribution Workflow

Since this project is used to learn GitHub collaboration:

Fork the repository or create a new branch (git switch -c feature-name).

Make your changes and commit them (git commit -m "Added new feature").

Push to your branch (git push origin feature-name).

Open a Pull Request for review.
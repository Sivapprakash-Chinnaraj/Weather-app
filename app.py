from flask import Flask, render_template, request, jsonify
import sqlite3
import os

app = Flask(__name__)
DB_PATH = os.path.join(app.root_path, 'instance', 'weather.db')

# Ensure the instance folder exists before creating the database
os.makedirs(os.path.join(app.root_path, 'instance'), exist_ok=True)

def init_db():
    """Creates the SQLite database file and the searches table if they do not exist."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS searches (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city_name TEXT NOT NULL,
            search_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    # Serves the index.html file from your templates/ folder
    return render_template('index.html')

@app.route('/save_search', methods=['POST'])
def save_search():
    # Receives the city name from your frontend JavaScript and saves it to SQLite
    data = request.get_json()
    city = data.get('city')
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO searches (city_name) VALUES (?)', (city,))
    conn.commit()
    conn.close()
    
    return jsonify({"status": "success", "saved_city": city})

@app.route('/history', methods=['GET'])
def get_history():
    # Retrieves the 5 most recent weather searches to display on the frontend
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT city_name, search_date FROM searches ORDER BY search_date DESC LIMIT 5')
    rows = cursor.fetchall()
    conn.close()
    
    # Formats the SQL rows into a JSON dictionary for JavaScript to read
    return jsonify([{"city": row[0], "date": row[1]} for row in rows])

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
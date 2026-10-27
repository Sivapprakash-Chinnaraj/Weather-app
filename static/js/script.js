// Load search history from the database when the page opens
document.addEventListener("DOMContentLoaded", loadHistory);

async function getWeather() {
    const city = document.getElementById('cityInput').value;
    if (!city) return;

    // Fetch from OpenWeatherMap (Replace 'YOUR_API_KEY' with your free key)
    const apiKey = '072a197180025808dc3d0e4963ef421e'; 
    const weatherUrl = `https://api.openweathermap.org/data/2.5/weather?q=${city}&units=metric&appid=${apiKey}`;
    
    try {
        const response = await fetch(weatherUrl);
        const data = await response.json();
        
        if (response.ok) {
            // Display weather in the HTML
            document.getElementById('weatherResult').innerHTML = `
                <h2>${data.name}</h2>
                <p>Temperature: ${data.main.temp}°C</p>
                <p>Conditions: ${data.weather[0].description}</p>
            `;
            
            // Send the successful city search to the Python backend
            saveSearch(data.name);
        } else {
            document.getElementById('weatherResult').innerHTML = '<p>City not found.</p>';
        }
    } catch (error) {
        console.error("Error fetching weather:", error);
    }
}

async function saveSearch(cityName) {
    // Sends a POST request to app.py
    await fetch('/save_search', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ city: cityName })
    });
    loadHistory(); // Refresh the history list on the screen
}

async function loadHistory() {
    // Requests the recent searches from app.py
    const response = await fetch('/history');
    const history = await response.json();
    
    const historyList = document.getElementById('historyList');
    historyList.innerHTML = ''; // Clear old list
    
    // Add each database row to the HTML list
    history.forEach(item => {
        const li = document.createElement('li');
        li.textContent = `${item.city} - ${item.date}`;
        historyList.appendChild(li);
    });
}

// Its working! You can now search for a city, and the search history will be saved in the database and displayed on the page.  
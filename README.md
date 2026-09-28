# weather_app

A beginner-friendly Python weather application that uses the Open-Meteo API to retrieve current weather information for a city.

Features
Search for any city
Get the current temperature
Get the current humidity
Handles cities that cannot be found
Technologies Used
Python
Requests library
Open-Meteo API
JSON
How It Works
The user enters a city name.
The Geocoding API converts the city name into latitude and longitude.
The Weather API uses these coordinates to retrieve current weather data.
The program extracts the temperature and humidity from the JSON response.
The results are displayed in the terminal.
What I Learned

Example
Enter a city: Tunis

The temperature is 27.4 °C
The humidity is 58 %
API

This project uses the Open-Meteo API for geocoding and weather data.

Future Improvements
Add wind speed
Add weather conditions
Add a graphical user interface
Improve error handling

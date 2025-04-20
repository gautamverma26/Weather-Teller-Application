# Weather-Teller-Application

Description The Weather Teller application is a simple, user-friendly program designed to provide real-time weather information for any city in the world. Built using Python, this application leverages the power of the OpenWeatherMap API to fetch live weather data and displays it in a clear and concise format. Whether you’re planning your day, traveling, or simply curious about the weather in another location, this program ensures you have the information you need at your fingertips.

The program focuses on providing essential weather details, including the current temperature (in Celsius), humidity levels, and a brief description of the weather conditions. Its modular structure, error-handling capabilities, and intuitive design make it a reliable and effective tool for retrieving weather information.

Features The Weather Teller program includes several key features to enhance user experience:

City-Based Weather Information: Users can input the name of any city in the world to receive accurate and up-to-date weather details. Detailed Weather Data: The program displays: Weather description (e.g., "clear sky" or "light rain"). Current temperature in Celsius. Humidity percentage. Error Handling: The application is designed to handle common errors gracefully, including: Invalid city names, providing a user-friendly message when the city cannot be found. Network issues, alerting the user if the API cannot be reached. Modular Design: The program is structured into reusable functions, each performing a specific task. This makes the code easier to understand, maintain, and test. Unit Testing: The application is accompanied by a test_project.py file containing unit tests for the core functions, ensuring that the program operates correctly under various conditions. Project Structure The Weather Teller project consists of two main files:

project.py This file contains the main logic of the application and is divided into three reusable functions:
fetch_weather: This function retrieves raw weather data from the OpenWeatherMap API. It takes the city name as input and sends an HTTP GET request to the API endpoint. The response is returned as a JSON object, which includes all the weather-related data for the specified city.

extract_weather_info: Once the raw JSON data is retrieved, this function processes and formats it. It extracts specific details, such as the city name, weather description, temperature, and humidity, organizing the data into a clean format for display.

display_weather: This function takes the formatted weather information and outputs it to the user in a readable format. It ensures the data is presented clearly, showing all relevant details like temperature, humidity, and the weather description.

How It Works To use the Weather Teller application:

Run the project.py script in your Python environment. Enter the name of any city when prompted. The application fetches the data from the API, processes it, and displays: A brief weather description. Current temperature in Celsius. Humidity percentage. If an invalid city name is entered, or there’s a network issue, the program will display an appropriate error message. The modular design, clean output, and reliable performance make Weather Teller a practical tool for real-time weather updates.

import requests

def main():
    while True:
        print("\nWeather Teller Application")
        print("1. Get weather for a city")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            city = input("Enter city name: ")
            weather_data = fetch_weather(city)
            if weather_data:
                extracted_data = extract_weather_info(weather_data)
                if extracted_data:
                    display_weather(extracted_data)
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


def fetch_weather(city):

    API_KEY = "c1c4183f395944f9bf8808a96c1ecbce"
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(URL)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException:
        print("Error: Unable to fetch weather data. Please check your internet connection.")
        return None


def extract_weather_info(data):

    try:
        weather = data["weather"][0]["description"].capitalize()
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        city_name = data["name"]
        return {"weather": weather, "temp": temp, "humidity": humidity, "city_name": city_name}
    except KeyError:
        print("Error: City not found. Please enter a valid city name.")
        return None


def display_weather(weather_data):

    print(f"\nWeather in {weather_data['city_name']}:")
    print(f"- Description: {weather_data['weather']}")
    print(f"- Temperature: {weather_data['temp']} °C")
    print(f"- Humidity: {weather_data['humidity']}%")


if __name__ == "__main__":
    main()


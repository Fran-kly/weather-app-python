import requests

API_KEY = "2a86cf3932377f27534e922eed4d6e0c"

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    response = requests.get(url)
    data = response.json()

    if data["cod"] != 200:
        print("City not found.")
        return

    city_name = data["name"]
    temp = data["main"]["temp"]
    weather = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]

    print(f"\nWeather in {city_name}:")
    print(f"Temperature: {temp}°C")
    print(f"Condition: {weather}")
    print(f"Humidity: {humidity}%")

def main():
    while True:
        print("\n ---- Welcome to the WEATHER APP ----")
        city = input("Enter city name (or type 'exit' to quit): ")

        if city.lower() == "exit":
            print("Goodbye!")
            break

        get_weather(city)

if __name__ == "__main__":
    main()
import requests

api_key = "d5fc2909cb5267d92185c53eb2a7839a"

print("===== Arya's Weather App =====")
print("Enter 'exit' anytime to quit the program.\n")
while True:
    city = input("Enter city name: ")
    if city.lower() == "exit":
        print("Exiting Weather App.")
        break
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data.get("cod") != 200:
        print("City not found. Try again.\n")
        continue

    temp = data["main"]["temp"]
    weather = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]
    wind_speed = data["wind"]["speed"]

    print(f"\nWeather in {city}:")
    print(f"Temperature: {temp} °C")
    print(f"Condition: {weather}")
    print(f"Humidity: {humidity}%")
    print(f"Pressure: {pressure} hPa")
    print(f"Wind Speed: {wind_speed} m/s\n")

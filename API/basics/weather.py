import requests

api_key = "46c4e5c055af69cc3036ef7e3e85bbef"
city = input("Which city do you want to know about? ")

url = f"https://openweathermap.org{city}&appid={api_key}&units=metric"

response = requests.get(url)

print(response.status_code)

if response.status_code == 200:
    data = response.json()
    
    city_name = data["name"]
    country = data["sys"]["country"]
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]

    print(f"\nWeather for {city_name}, {country}")
    print(f"Condition: {description}")
    print(f"Temperature: {temp}°C")
    print(f"Feels Like: {feels_like}°C")
    print(f"Humidity: {humidity}%")
else:
    print(f"Error{response.status_code})")
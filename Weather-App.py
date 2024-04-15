import requests

api_key = "da898e16f83e74f5007ed2ad64c08732"

city_name = input("Enter the City: ")

weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}")

weather = weather_data.json()['weather'][0]['main']
temp = weather_data.json()['main']['temp']
print("-------------------------------git")
print(f"The weather in {city_name} is {weather} |")
print("-------------------------------")
print("\n")
print("-----------------------------------------")
print(f"The temperature in {city_name} is {temp} ˚F  |")
print("-----------------------------------------")
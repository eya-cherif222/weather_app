import requests
city=input("enter a city:")
geo= requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en&format=json")
geod=geo.json()
if geod.get("results"):
    latitude=geod["results"][0]["latitude"]
    longitude=geod["results"][0]["longitude"]
else:
    print("city not found")
response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,relative_humidity_2m")
data=response.json()
temperature = data["current"]["temperature_2m"]
print("The temperature is", temperature, "°C")
humidity=data["current"]["relative_humidity_2m"]
print("The humidity is:",humidity,"%")

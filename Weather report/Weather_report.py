import requests, json


# base URL
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
CITY = input("What city are you in? ")
API_KEY = #put your API key here
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY + "&units=imperial"
response = requests.get(URL)
if response.status_code == 200:
   info = json.loads(response.text)
   data = response.json()
   main = data['main']
   temperature = main['temp']
   humidity = main['humidity']
   pressure = main['pressure']
   low = main['temp_min']
   high = main['temp_max']
   visibility = (float(info['visibility'])/1000)
   report = data['weather']
   print(f"{CITY:-^30}")
   print(f"Temperature: {temperature}" + "°F")
   print(f"Today's high: {high}" + "°F")
   print(f"Today's low: {low}" + "°F")
   print(f"Humidity: {humidity}" + "%")
   print(f"Pressure: {pressure}" + "hPa")
   print(f"Visibility: {visibility}" + "miles")
   print(f"Weather Report: {report[0]['description']}")
else:
   print("Error - please enter a valid city name")

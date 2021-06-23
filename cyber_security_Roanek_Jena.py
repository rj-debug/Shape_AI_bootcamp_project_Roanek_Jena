import requests
from datetime import datetime
import simplejson as json

api_key = '9c81e9a16bf7f8245ff0fa3838375055'
location = input("Enter the city name:")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")


print("----------------------------------------------------------")
print("Weather stats for - {}  ||  {}".format(location.upper(), date_time))
print("----------------------------------------------------------")

print("Current temperature is: {:.2f} deg C".format(temp_city))
print("Current weather desc :",weather_desc)
print("Current Humidity :",hmdt, '%')
print("Current Wind Speed :",wind_spd,'kmph')


print()
x=print("Weather stats for - {}  ||  {}".format(location.upper(), date_time))
y=print("Current temperature is: {:.2f} deg C".format(temp_city))
z=print("Current weather desc :",weather_desc)
a=print("Current Humidity :",hmdt, '%')
b=print("Current Wind Speed :",wind_spd,'kmph')

my_records = {"weather stats:":x,
              "temperature:":y,
              "weather desc:":z,
              "humidity:":a,
              "wind speed:":b}

json_obj = json.dumps(my_records)

with open("cyber_security_rj.txt","w") as f:
  f.write(json_obj)
  f.close()

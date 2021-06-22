import requests
from datetime import datetime

message=""
api_key = '87d845b0b6cf29baa1a73cc34b067a95'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

#creating a string to be writen in the text file
message ="------------------------------------------------------------\nWeather Stats for - "+location.upper()+" || "+date_time+"\n-------------------------------------------------------------\nCurrent temperature is: "+str(temp_city)+"deg C\nCurrent weather desc  : "+weather_desc+"\nCurrent Humidity      : "+str(hmdt)+"%\nCurrent wind speed    : "+str(wind_spd)+" kmph\n"

#create text file and write in the text file
with open ('weather.txt','w') as f:
    f.write(str(message))

#read the file and print the content
with open ('weather.txt','r') as f:
    mes=f.read()
    print(mes)


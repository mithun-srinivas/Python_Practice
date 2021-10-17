
from flask import Flask,render_template,request,abort
# import json to load json data to python dictionary
import json
# urllib.request to make a request to api
import urllib.request
import pyttsx3

def weather(city):
    api_key = '48a90ac42caa09f90dcaeee4096b9e53'
    

    # source contain json data from api
    try:
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid='+api_key).read()
    except:
        return "Check The City Name Given"
    # converting json data to dictionary

    list_of_data = json.loads(source)

    # data for variable list_of_data
    data = {
        "country_code": str(list_of_data['sys']['country']),
        "coordinate": str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']),
        "temp": str(list_of_data['main']['temp']) + 'k',
        #"temp_cel": tocelcius(list_of_data['main']['temp']) + 'C',
        "pressure": str(list_of_data['main']['pressure']),
        "humidity": str(list_of_data['main']['humidity']),
        "cityname":str(city),
    }
    engine = pyttsx3.init()
    engine.say("The weather Report at "+ str(city) + "says that the temperature is at"+str(list_of_data['main']['temp'])  + "kelvin" +"with the humidity of"+str(list_of_data['main']['humidity'])+"and pressure "+str(list_of_data['main']['pressure']))
    engine.setProperty('rate',1)
    engine.setProperty('volume', 0.9)
    engine.runAndWait()

city=input("Enter The City Name :")
weather(city)
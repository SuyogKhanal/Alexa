import pyttsx3
import pywhatkit
import datetime
import pyjokes
import wikipedia
import sys
import requests
import webbrowser

def engine_talk(text):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

def weather(city):
    api_key = "b2dc8435b1235cbd6d7e246fa03b268a"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = city
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
    response = requests.get(complete_url) 
    x = response.json() 
    if x["cod"] != "404": 
        y = x["main"] 
        current_temperature = y["temp"] 
        temp_in_celcius = current_temperature - 273.15
        return str(int(temp_in_celcius))
    

def run_alexa(command):

    if 'play a song' in command:
        song = 'Arijit Singh'
        engine_talk('Playing some music')
        pywhatkit.playonyt(song)
    elif 'open youtube' in command:
        webbrowser.open("youtube.com")

    elif 'open google' in command:
        webbrowser.open("google.com")

    elif 'open facebook' in command:
        webbrowser.open("facebook.com")
    elif 'play' in command:
        song = command.replace('play', '')
        engine_talk('Playing....' + song)
        pywhatkit.playonyt(song)     
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        engine_talk('Current Time is ' + time)
    elif 'joke' in command:
        get_j = pyjokes.get_joke()
        engine_talk(get_j)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        engine_talk(info)
    elif 'weather' in command:
        city = 'Hong Kong'
        engine_talk('The temperature in Hong Kong is ' + weather(city) + ' degree Celsius')
    elif 'stop' in command:
        engine_talk("Good bye")
        sys.exit()
    else:
        engine_talk("I didn't hear you properly")
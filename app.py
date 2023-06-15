from flask import Flask, render_template, redirect
import warnings
warnings.filterwarnings('ignore')
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import pyjokes
import wikipedia
import sys
import requests, json 

listener = sr.Recognizer()

app = Flask("__name__")

def engine_talk(text):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

def user_commands():
    try:
        with sr.Microphone() as source:
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            command = command.replace('alexa', '')
    except:
        pass
    return command

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

def run_alexa():
    command = user_commands()
    if 'play a song' in command:
        song = 'Arijit Singh'
        engine_talk('Playing some music')
        pywhatkit.playonyt(song)
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

@app.route('/')
def hello():
    return render_template("index.html")

@app.route("/", methods=['POST', 'GET'])
def submit():
    while True:
        run_alexa()
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

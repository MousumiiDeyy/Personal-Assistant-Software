import pyttsx3
import datetime
import os
import wikipedia
import speech_recognition as sr
import random
import webbrowser
#import pywhatkit as wk
import requests
from bs4 import BeautifulSoup

engine = pyttsx3.init()
voices = engine.getProperty('voices')
voice = voices[1]
engine.setProperty('voice', voice.id)
print(voices[1])
newVoiceRate = 150
engine.setProperty("rate",newVoiceRate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    
    except Exception as e:
        print("say that again please...")
        speak("Please say againn")
        return "None"
    return query

def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour <18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("Jarvis at your command. what can i do?")


if __name__ == "__main__":
    while True:
        query = takecommand().lower()
        if "wake up" in query:
            wishme()

            while True:
                query = takecommand().lower()
                if "offline" in query:
                    speak("ok, you can call me anyime")
                    break

                elif "hello" in query:
                    speak("Hello, How are you?")
                elif "i am fine" in query:
                    speak("Thats great")
                elif "how are you" in query:
                    speak("perfect")
                elif "thank you" in query:
                    speak("You are welcome")

                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                    
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)

                elif "google" in query:
                    from searchnow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from searchnow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from searchnow import searchWikipedia
                    searchWikipedia(query)
                
                elif "temperature" in query:
                   search = "temperature in kolkata" 
                   url = f"https://www.google.com/search?q={search}"
                   r = requests.get(url)
                   data = BeautifulSoup(r.text, "html.parser")
                   temp = data.find("div", class_ = "BNeawe").text
                   speak(f"Current{search} is {temp}")

                elif "weather" in query:
                   search = "weather in kolkata" 
                   url = f"https://www.google.com/search?q={search}"
                   r = requests.get(url)
                   data = BeautifulSoup(r.text, "html.parser")
                   temp = data.find("div", class_ = "BNeawe").text
                   speak(f"Current{search} is {temp}")

                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"The time is {strTime}")
                
                elif "sleep" in query:
                    speak("Going to sleep")
                    exit()

                

                elif "set an alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("Set the time")
                    a = input("Please tell the time :- ")
                    alarm(a)
                    speak("Done")




                

import pyttsx3
import datetime
import os
import wikipedia
import speech_recognition as sr
import random
import webbrowser
import pywhatkit as wk

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
newVoiceRate = 150
engine.getProperty('voices')
engine.setProperty('rate',newVoiceRate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("Today the date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour <18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("Jarvis at your command. what can i do?")

def takecommand():

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    
    except Exception as e:
        print("say that again please...")
        speak("Please say againn")
        return "None"
    return query


if __name__ == "__main__":
    wishme()
    while True:
        query=takecommand().lower()
        if 'jarvis' in query:
            print("yes")
            speak("Yes")

        elif "Who are you" in query:
            print("My name is jarvis")
            speak("My name is Jarvis")
            print("i can do everything which pompom programmed me to do")
            speak("i can do everything which pompom programmed me to do")

        elif "who made you" in query:
            print("I am created by the magic of python which was coded in a mystical manner.. by Pompom")
            speak("I am created by the magic of python which was coded in a mystical manner.. by Pompom")
        
        elif 'what is' in query:
            speak('What should I search ?')
            qry = takecommand().lower()
            webbrowser.open(f"{qry}")
            results = wikipedia.summary(qry, sentences=1)
            speak(results)

        elif "just open youtube" in query:
            webbrowser.open('youtube.com')
        
        elif "open youtube" in query:
            speak("what do you like to watch ?")
            qrry = takecommand().lower()
            wk.playonyt(f"{qrry}")
        
        elif "search on youtube" in query:
            query = query.replace("search on youtube", "")
            webbrowser.open(f"www.youtube.com/results?search_query={query}")

        elif "close browser" in query:
            os.system("taskkill /f /im msedge.exe")

        elif "close chrome" in query:
            os.system("taskkill /f /im chrome.exe")

        #elif "open paint" in query:
        #    npath = "C:\Users\mousu\AppData\Local\Microsoft\WindowsApps\Microsoft.Paint_8wekyb3d8bbwe\mspaint.exe"
        #    os.startfile("npath")

        elif "close paint" in query:
            os.system("taskkill /f /im mspaint.exe")

        elif "open notepad" in query:
            npath = "C:\Windows\notepad.exe"
            os.startfile(npath)
        
        elif "close notepad" in query:
            os.system("taskkill /f /im notepad.exe")

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "close command prompt" in query:
            os.system("taskkill /f /im cmd.exe")

        elif "tell the time" or "what is the time" or "what is time now" or "what is the current time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")

        elif "date" in query:
            date()
        
        elif "offline" in query:
            speak("Bye Maam")
            quit()
        
 
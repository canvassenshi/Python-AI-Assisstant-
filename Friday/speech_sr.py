import speech_recognition as sr
import pyttsx3
import pywhatkit as pyk
import requests 
from playsound import playsound
import os
import time
import webbrowser


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 175)


files = os.listdir("C:/Users/ivarn/Desktop/")
file_names = map(lambda x: x.lower(), files)
file_list = list(file_names)


def runapp(app):
    for file in file_list:
        if app in file:
            os.startfile(f"C:/Users/ivarn/Desktop/{file}")
        
            

def dictionary(word):
    URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"
    data = requests.get(URL + word)
    data = data.json()
    dic = data[0]["meanings"][0]["definitions"][0]
    meaning, example = dic["definition"], dic["example"]
    return [meaning, example]


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "friday" in command:
                command = command.replace("friday", "")
    except:
        pass
    return command

def friday():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pyk.playonyt(song)
    elif "hello" in command:
        talk("hi, i am friday")
    elif "what is" in command:
        command = command.replace("what is", "")
        words = dictionary(command)
        print(words[0])
        talk(command + "is" + words[0] + "for example" + words[1])
    elif "fart" in command:
        talk("welcome to my world...")
        playsound("fart.mp3")
    elif "best" in command:
        talk("yana is the best ofcourseeeeee 10/10")
    elif "search" in command:
        command = command.replace("search", "")
        pyk.search(command)
    elif "open" in command:
        command = command.replace("open", "")
        command = command.strip()
        webbrowser.open_new_tab(f"https://www.{command}.com")
        # try:
        #     runapp(command)
        # except Exception as e:
        #     print(e)

friday()



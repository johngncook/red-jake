import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import re


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish_Me():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak ("Good Morning!")
    elif hour >= 12 and hour <18:
        speak("Good Afternoon")
    else:
        speak ("Good Evening!")

    speak (" I am Jarvis Sir. How may I help you today?")


# Takes micrphone input and returns string output
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio)
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"

    return query


if __name__ == "__main__":
    wish_Me()
    while True:
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak('What would you like to lookup?')
            lookup_query = takecommand().lower()
            speak('Searching Wikipedia')
            results = wikipedia.summary(lookup_query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open reddit' in query:
            reg_ex = re.search('open reddit (.*)', query)
            url = 'https://www.reddit.com/'
            if reg_ex:
                subreddit = reg_ex.group(1)
                url = url + 'r/' + subreddit
            webbrowser.open(url)
            sofiaResponse('The Reddit content has been opened for you Sir.')

        elif 'open youtube' in query:
             webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com/")

        elif 'open maps' in query:
            webbrowser.open("https://www.google.com/maps")

        elif 'open blog' in query:
            jarvis_path = "C:\\Users\\johns\\mango_tree\\mango_tree\\settings.py"
            os.startfile(jarvis_path)


        else:
            if 'stop' or 'enough' or 'I am good' in query:
                speak('That is good to hear sir.')
                speak('If you need assistance, please let me know!')
                exit()


    # Logic for executing tasks based on query



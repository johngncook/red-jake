import pyttsx3
import datetime
import speech_recognition as sr
import wolframalpha


engine = pyttsx3.init('sapi5')
app_id = 'L73LGW-35VJW9WY6J'
client = wolframalpha.Client(app_id)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    """Greets user depending on time of day."""
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak ("Good Morning!")
    elif hour >= 12 and hour <18:
        speak("Good Afternoon")
    else:
        speak("Good Evening!")

    speak(" I am Jake Sir. Red Jake. How may I help you today?")



def take_command():
    """Takes microphone input and returns string output."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
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

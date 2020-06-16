import wikipedia
import webbrowser
import re

from app_functions import *


if __name__ == "__main__":
    wish_Me()
    while True:
        """Loop to choose a command."""
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
            speak('The Reddit content has been opened for you Sir.')

        elif 'open youtube' in query:
             webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com/")

        elif 'open maps' in query:
            webbrowser.open("https://www.google.com/maps")


        else:
            if 'stop' or 'enough' or 'I am good' in query:
                speak('That is good to hear sir.')
                speak('If you need assistance, please let me know!')
                exit()


    # Logic for executing tasks based on query



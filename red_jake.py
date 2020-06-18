import wikipedia
import webbrowser
import re


from app_functions import *


if __name__ == "__main__":
    greet()
    while True:
        """Loop to choose a command."""
        query = take_command().lower()
        if 'wikipedia' in query:
            speak('What would you like to lookup?')
            lookup_query = take_command().lower()
            speak('Searching Wikipedia')
            results = wikipedia.summary(lookup_query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'reddit' in query:
            reg_ex = re.search('open reddit (.*)', query)
            url = 'https://www.reddit.com/'
            if reg_ex:
                subreddit = reg_ex.group(1)
                url = url + 'r/' + subreddit
            webbrowser.open(url)
            speak('The Reddit content has been opened for you Sir.')

        elif 'youtube' in query:
             webbrowser.open("https://www.youtube.com/")
             speak('youtube has been opened for you sir.')

        elif 'google' in query:
            webbrowser.open("https://www.google.com/")
            speak('google has been opened for you sir.')


        elif 'maps' in query:
            webbrowser.open("https://www.google.com/maps")
            speak('google maps has been opened for you sir.')

        elif 'question' in query:
            speak('What would you like to know?')
            while True:
                question_query = take_command().lower()
                if 'open a webpage' in question_query:
                    speak('What would you like to open up?')
                    break
                else:
                    res = client.query(question_query)
                    try:
                        answer = next(res.results).text
                    except Exception:
                        speak('That did not work, ask me something else.')

                    else:
                        speak(answer)
                        speak('What else would you like to know?')



        else:
            if 'stop' or 'enough' or 'I am good' in query:
                speak('That is good to hear sir.')
                speak('If you need assistance, please let me know!')
                exit()



    # Logic for executing tasks based on query



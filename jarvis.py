import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import spotify


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('good morning!')
    elif hour>=12 and hour<15:
        speak("good afternoon!")
    else:
        speak('good evening!')
    speak("i am nikita , mam . How may i help you?")
def takecommand():
    #it takes microphone input from the user and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('listening ...')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Recognising . . .')
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Please repeat it ...")
        return 'none'
    return query


if __name__ == '__main__':
    wishme()
    while True:
        query = takecommand().lower()
        #  logic for executing tasks based on query 
        if 'wikipedia' in query:
            speak('Searching Wikipedia . . .')
            query = query.replace('wikipedia',"")
            results = wikipeqdia.summary(query, sentences=1)
            speak('According to Wikipedia') 
            print(results)
            speak(results)
            print('action completed !!!\n')

        elif 'open youtube' in query:
            print('opening. . .')
            webbrowser.open('youtube.com')
            print('action completed !!!\n')

        elif 'open google' in query:
            print('opening. . .')
            webbrowser.open('google.com')
            print('action completed !!!\n')

        elif 'open bing' in query:
            print('opening. . .') 
            webbrowser.open('bing.com')
            print('action completed !!!\n')
        
        elif 'open stackoverflow' in query:
            print('opening. . .')
            webbrowser.open('stackoverflow.com')
            print('action completed !!!\n')
        
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir , the time is {strTime}")
            print('action completed !!!\n')

        else:
            exit()
            
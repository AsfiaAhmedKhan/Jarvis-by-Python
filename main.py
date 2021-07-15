import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good morning')
    elif hour>12 and hour<18:
        speak('Good Afternoon')
    elif hour>=18 and hour<24:
        speak('Good evening')

    speak("I am Asfia Please tell me how may I help you")

def take_command():
    #it takes microphone input from the user and gives string output
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold= 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please")
        return "None"
    return query



if __name__== "__main__":
    wishMe()
    while True:
        query = take_command().lower()


        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia"," ")
            results= wikipedia.summary(query,sentence=2)
            speak("According to wikipedia")
            print(results)
            speak(results)





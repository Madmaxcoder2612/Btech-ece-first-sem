import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices',voices[0].id)

def speak(audio):
  engine.say(audio)
  engine.runAndWait()


def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    
    else:
        speak("Good Evening!")

    speak("I am JARVIS, Sir. Please tell me, How may I help you ")
    
def takeCommand():
    #It takes microphone input from the user and returns the string output.

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listerning...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)

        print("Say that again please...")
        return "None"
    return query

    def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('youremail@gmail.com', 'your-password-here')
        server.sendmail('youremail@gmail.com', to, content)
        server.close()


if __name__=="__main__":
     WishMe()
     while True:
        #if 1:
        query = takeCommand().lower()

     # Logic for executing tasks nased on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak('Opening Youtube, sir...')
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak('Opening googel, sir...')
            webbrowser.open("google.com")

        elif 'open education' in query:
            speak('Opening UMS, sir...')
            webbrowser.open("ums.lpu.in")

        elif 'open water system' in query:
            speak('Opening Water Management System...')
            webbrowser.open("https://console.firebase.google.com/u/0/project/water-management-system-8ab48/settings/serviceaccounts/databasesecrets")


        elif 'play music' in query:
            speak('Playing the music, sir...')
            music_dir = 'C:\\Users\\HP\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            
        elif 'email to flash' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = ""
                #sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend madmax, I am not able to send this email")

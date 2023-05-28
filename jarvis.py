#####jarvis Assistent
####Import Libraries
import pyttsx3 #pip install pyttsx3
import datetime
import sys
import wikipedia
import speech_recognition as sr
import smtplib
import webbrowser as wb
import os
import psutil
import pyjokes

engine = pyttsx3.init()
voices = engine.getProperty('voices')


def speak(audio, lang= 'en'):
    # Select a female voice based on the index
    # Set the language for the voice
    engine.setProperty('voice', None)  # Reset voice selection
    engine.setProperty('language', lang)
    female_voice_index = 1  # Change the index based on available voices
    if female_voice_index < len(voices):
        engine.setProperty('voice', voices[female_voice_index].id)
    else:
        print("Invalid voice index")

    engine.say(audio)
    engine.runAndWait()

#speak("This Is Jarvis AI Assistant")

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)

#time() 

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)

#date()  

def wishme():
    speak("Welcome back sir!")
    time()
    date()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour<12:
        speak("Good Morning Sir!")
    elif hour >=12 and hour<18:
        speak("Good afternoon sir!")
    elif hour >=18 and hour<24:
        speak("Good Evening Sir!")
    else:
        speak("Good night sir!")
    speak("I am your voice assistant. Please tell me how can i help you")

#wishme()

def takeCommand():
    # Create a recognizer object
    r = sr.Recognizer()
    # Define the microphone as the audio source
    microphone = sr.Microphone()
    print("Listening...")

    # Listen to the microphone input
    with microphone as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        # Recognize speech using Google Speech Recognition
        print("Recongnizning...")
        query = r.recognize_google(audio)
        print(query)
        # Check if the task is completed
        if query == "offline" or query == "go offline":
            print("Task completed. Exiting the program.")
            sys.exit()
            
        return query
    except Exception as e:
        print("Sorry, I didn't catch that. Please say again.")
        return "None"

#takeCommand()

def introduce():
    speak("I am Jarvis, an AI language model developed by Rakesh Engineer.")
    speak("I am designed to assist with answering questions, providing information, and engaging in conversation.")
    speak("My purpose is to help users by providing helpful and informative responses.")

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('abc@gmail.com','123')
    server.sendmail('abzc@gmail.com', to, content)
    server.close()

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at' +usage)
    battery = psutil.sensors_battery()
    speak("Battery ia at")
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())

def thanks():
    speak("You're welcome!")
#thanks()

def hello():       
    speak("Hello! I'm doing great. How about you?")
#hello()

if __name__ == "__main__":
    #wishme()
    while True:
        query = takeCommand().lower()
        if 'time' in query:
            time()
        elif 'date' in query:
            date() 
        elif 'who are you' in query:
            introduce()
        elif 'thanks' in query or 'thank you' in query:
            thanks()
        elif 'hello' in query or 'how are you' in query:
            hello()
        elif 'wikipedia' in query:
            speak("Searching...") 
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)  
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = 'xyz@gmail.com'
                #sendEmail(to,content)
                speak(content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Unable to send the email") 
        elif 'search in chrome' in query:
            speak("what should i search?")
            chromepath = 'C:\Program Files\Google\Chrome\Application/chrome.exe %s'
            search = takeCommand().lower() 
            wb.get(chromepath).open_new_tab(search+'.com')
        #elif 'logout' in query:
        #    os.system("shutdown -l")
        #elif 'shutdown' in query:
        #    os.system("shutdown /r /t 1")
        #elif 'restart' in query:
        #    os.system("shutdown /r /t 1") 
        elif 'play songs' in query:
            speak("OK sir, opening a playlist...")
            songs_dir = 'D:\Music'
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))               
        elif 'remember that' in query:
            speak("What should i remember?")
            data = takeCommand()
            speak("you said me to remember that"+data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close()
        elif 'do you remember anything' in query:
            remember = open('data.txt','r')
            speak("you said me to remember that" +remember.read())
        elif 'cpu' in query:
            cpu()  
        elif 'joke' in query:
            jokes()              
        elif 'ofline' in query:
            quit()
        


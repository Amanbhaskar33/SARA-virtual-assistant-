import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import pyjokes
import wikipedia
import JarvisAI
import re
import pprint

obj = JarvisAI.JarvisAssistant()


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


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
            if 'sara' in command:
                command = command.replace('sara', '')
                print(command)
    except:
        print("I didn't understant try again!")
    return command


def run_sara():
    command = take_command()
    print(command)
    if re.search('weather|temperature', command):
        news = command.split(' ')[-1]
        weather_res = obj.weather(news)
        print(weather_res)
        talk(weather_res) 
    elif re.search('news', command):
        news_res = obj.news()
        pprint.pprint(news_res)
        talk(f"I have found {len(news_res)} news. You can read it. Let me tell you first 2 of them")
        talk(news_res[0])
        talk(news_res[1])    
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'what is' in command:
        information = command.replace('What is','')
        intro = wikipedia.summary(information,1)
        print(intro)
        talk(intro)
    elif 'date' in command:
        date = datetime.datetime.now().strftime("%d-%B-%Y")
        talk("Today's date is " + date)
        print(date)
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)
    else:
        talk('Please say the command again.')

while True:
    run_sara()

import speech_recognition as sr
import datetime
import pyttsx3
engine = pyttsx3.init()
import webbrowser
import os
import pywhatkit
import urllib.parse
import requests
from pyttsx3 import engine





def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def tell_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    say(f"Current time is {current_time}")

def listen():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        sr.pause_threshold = 2

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(f"user said {query}")
    except Exception as e:
        print("Say that again please...")
        return ""
    return query


if __name__ == "__main__":
    print('PyCharm')
    say("Hello i am Jarvis. Please tell me how can i help you?")

    while True:
        command = listen().lower()

        if "time" in command:
            tell_time()

        elif "open youtube" in command:
            say(f"Opening youtube...")
            webbrowser.open_new_tab("https://www.youtube.com/")


        elif "search on youtube" in command:
            say("what should i search?")
            query = command.replace("search on youtube", "").strip()
            say(f"searching for {query} on youtube...")
            search_url = (f"https://www.youtube.com/results?search_query={query}")
            webbrowser.open_new_tab(search_url)

        elif "search on google" in command:
            say("What would you like me to search for?")
            search_query = listen()
            url = f"https://www.google.com/search?q={search_query}"
            webbrowser.open_new_tab(url)
            say("Here are the search results.")

        elif "send message on whatsapp" in command:
            say("Who should I send the message to?")
            receiver = input("Enter number with country code: ")
            say("What is the message?")
            message = listen()
            pywhatkit.sendwhatmsg_instantly(receiver, message, 15)
            say("I've sent that message for you.")

        elif "open google" in command or "google khol de bhai" in command:
            say("Opening Google...")
            webbrowser.open_new_tab("https://www.google.com")

        elif "date" in command:
            now = datetime.datetime.now()
            date_string = now.strftime("%m/%d/%Y")
            say(f"today's date is {date_string}")

        elif "who am i" in command or "main kaun hun" in command:
            say("you are my master gungun mukati!")

        elif "open wikipedia" in command or "wikipedia khol de bhai" in command:
            say(f"opening wikipedia...")
            webbrowser.open_new_tab(":https://en.wikipedia.org/wiki/")

        elif "open netflix" in command or "khul ja netflix" in command:
            say(f"opening netflix...")
            webbrowser.open_new_tab("https://www.netflix.com/")

        elif "who are you " in command or "hu r u"in command:
            say("me mere master , gungun mukati  ka personal ai assistant hu Jarvis ! ")

        elif "thank you" in command or "thank u" in command:
            say(f"welcome")

        elif "good bye"  in command or "goodbye" in command:
            say("Goodbye!")
            break
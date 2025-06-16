import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import wikipedia
import pyjokes
import sys
import random
# Initialize the voice engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        print(f"You: {command}")
        return command
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("Network error.")
        return ""
status_responses = ["Im doing great, thank you for asking!",
                    "Im doing wonderful, im sure you are too!",
                    "Im fantastic!",
                    "Im always trying to do better",
                    "Im doing great, I enjoy helping people!"]

def respond(command):
    # Responses:
    if "hi" in command:
        speak("Hello! How can I help you?")
    if 'how are you'in command:
        response = random.choice(status_responses)
        speak(response)
        print(response)
    elif "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {now}")
    elif "date" in command:
        today = datetime.date.today().strftime("%B %d, %Y")
        speak(f"Today is {today}")
    elif "joke" in command:
        joke = pyjokes.get_joke()
        speak(joke)
        
    # Web:
    elif "open" in command and "website" in command:
        site = command.replace("open", "").replace("website", "").strip()
        url = f"https://{site}.com"
        webbrowser.open(url)
        speak(f"Opening {site}")
    elif "open" in command:
        site = command.replace("open", "").strip()
        url = f"https://{site}.com"
        webbrowser.open(url)
        speak(f"Opening {site}")
    elif "search wikipedia for" in command:
        topic = command.replace("search wikipedia for", "").strip()
        try:
            result = wikipedia.summary(topic, sentences=2)
            speak(result)
        except:
            speak("Sorry, I couldn't find anything on Wikipedia.")
    elif "search google for" in command:
        query = command.replace("search google for", "").strip()
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
        speak(f"Searching Google for {query}")
    
    elif "bye" in command or "exit" in command:
        speak("Goodbye! Have a great day.")
        sys.exit()
    else:
        speak("Sorry, I don't understand that command.")

def main():
    speak("Voice assistant started.")
    while True:
        command = listen()
        if command:
            respond(command)

if __name__ == "__main__":
    main()

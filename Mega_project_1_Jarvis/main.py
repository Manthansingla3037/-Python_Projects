import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
from google import genai

r = sr.Recognizer()


def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id) 
    engine.setProperty('rate', 140)
    engine.say(text)
    engine.runAndWait()
    # engine.stop()

def aiProcess(command):
    client = genai.Client(api_key="AIzaSyCb4fb5PoX4rPTdPQIRKoGMX7Ih-WigZhw")

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=command,
    )

    return response.text

def processCommand(c):
    if "open google" in c.lower():
        speak("opening google")
        webbrowser.open("https://google.com")
    elif "open facecook" in c.lower():
        speak("opening facebook")
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        speak("opening youtube")
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        speak("opening linkedin")
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        musicLibrary.music[song]

    else:
        #let openai handle the command
        output = aiProcess(c)
        speak(output)

def takecommand():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source,timeout=3,phrase_time_limit=7)
            print("Recognizing...")
            text = r.recognize_google(audio)
            print(text)
            return text
    except Exception as e:
        print("speak again!")
        return None
        
if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        #listen for the wake word Jarvis and if it contains Jarvis then continuing
        word = takecommand()
        if word is None:
            continue
        if "jarvis" in word.lower():
            speak("Yes , How may i help you")
            print("Jarvis active....")
            #listen for command
            command = takecommand()
            if command is None:
                continue
            processCommand(command)
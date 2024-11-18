import pyttsx3
import speech_recognition


# engine = pyttsx3.init("sapi5")
# voices = engine.getProperty("voices")
# engine.setProperty("voice", "voice[0].id") # Set the voice
# engine.setProperty("rate",170)   # Speeed of voice


def speechtx(x):  # Function Text to Speech
    engine = pyttsx3.init() # Initializing Text to Speech engine  # init name class
    voice = engine.getProperty('voices')
    engine.setProperty('voice',voice[1].id) # Selecting the voice
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150) # Adjusting the speed of speech
    engine.say(x) # Saying the text #say Function
    engine.runAndWait() # Running the text to speech conversion


def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300  # Speed of your voice
        audio = r.listen(source,0,4) # Listen Up to 4 sec
        
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
        except Exception as e:            # If not recognized
            print("Say That again...")
            return "None"
    return query

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if 'Wake Up' in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if 'go to sleep' in query:
                    speechtx("OK sir , You can call me anytime") 
                    break

                elif "hello" in query:
                    speechtx("Hello sir, how are you? ")
                elif "i am fine" in query:
                    speechtx("thats good")
                elif "how are you" in query:
                    speechtx("I am fine, thank you. ")
                elif "Thank you" in query:
                    speechtx("You Welcome Sir")
                
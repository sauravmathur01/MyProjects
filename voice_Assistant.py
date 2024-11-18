# import pyttsx3 # Text to speech Convert
# import speech_recognition as sr
# import webbrowser
# import datetime
# import pyjokes
# import os
# import time

# def sptext():  # Function Speech Recognition
#     recognizer = sr.Recognizer() # Recognizer class for Speech Recognition
#     with sr.Microphone() as source: # Microphone
#         print("Listening...")
#         recognizer.adjust_for_ambient_noise(source) # for noise correction
#         audio = recognizer.listen(source) # Listen to the audio from the microphone # audio name variable
#         try:
#             print("Recognizing...")
#             data = recognizer.recognize_google(audio) # Recognize
#             print("You said: " + data)
#             return data
#         except sr.UnknownValueError:
#             print("Unable to recognize")
#             return "None"
#     return data

# # sptext()

# def speechtx(x):  # Function Text to Speech
#     engine = pyttsx3.init() # Initializing Text to Speech engine  # init name class
#     voice = engine.getProperty('voices')
#     engine.setProperty('voice',voice[1].id) # Selecting the voice
#     rate = engine.getProperty('rate')
#     engine.setProperty('rate', 150) # Adjusting the speed of speech
#     engine.say(x) # Saying the text #say Function
#     engine.runAndWait() # Running the text to speech conversion
# # speechtx("Hello, Welcome to My Project. I am your AI Assistant. How can I help you today?")

# if __name__ == "__main__":
    
#     # if sptext().lower() == "hey assistant" :
#         while True :
#             if  "hey assistant" in sptext().lower():
#                         from GreetMe import greetMe
#                         greetMe()

#             while True:
#                     data1=sptext().lower()




#                     if "your name" in data1:
#                         name = " my name is assistance"
#                         speechtx(name)
#                     elif "old are you" in data1:
#                         age = "I'm a simple AI asssistant, I don't have a real age."
#                         speechtx(age)
#                     elif "how are you" in data1:
#                         how = "I'm doing well, thank you for asking."
#                         speechtx(how)
#                     elif "how r u" in data1:
#                         howr = "I'm doing well, thank you for asking."
#                         speechtx(howr)
#                     elif "what's the weather like" in data1:
#                         weather = "I'm unable to provide real-time weather information."
#                         speechtx(weather)
#                     elif "time" in data1:
#                         current_time = datetime.datetime.now().strftime("%H:%M:%p")
#                         speechtx(current_time)
#                     elif "youtube" in data1:
#                         webbrowser.open("https://www.youtube.com")
#                     elif "Google+" in data1:
#                         webbrowser.open("https://plus.google.com")
#                     elif "google" in data1:
#                         webbrowser.open("https://www.google.com")
#                     elif "joke" in data1:
#                         joke = pyjokes.get_joke(language="en", category="neutral")
#                         print(joke)
#                         speechtx(joke)
#                     elif 'play song' in data1:
#                         add= "D:\MyProjects\Voice Assistance\Songs"
#                         listsong = os.listdir(add)
#                         print(listsong)
#                         os.startfile(os.path.join(add,listsong[0]))
#                     elif "bye" in data1:
#                         speechtx("Thank you for using my AI Assistant. Goodbye!")
#                         break

#                     time.sleep(4)
# else:
#     print("thanks")

# import pyttsx3  # Text to speech Convert
# import speech_recognition as sr
# import webbrowser
# import datetime
# import pyjokes
# import os
# import time

# def sptext():  # Function Speech Recognition
#     recognizer = sr.Recognizer()  # Recognizer class for Speech Recognition
#     with sr.Microphone() as source:  # Microphone
#         print("Listening...")
#         recognizer.adjust_for_ambient_noise(source)  # for noise correction
#         audio = recognizer.listen(source)  # Listen to the audio from the microphone
#         try:
#             print("Recognizing...")
#             data = recognizer.recognize_google(audio)  # Recognize
#             print("You said: " + data)
#             return data
#         except sr.UnknownValueError:
#             print("Unable to recognize")
#             return "None"

# def speechtx(x):  # Function Text to Speech
#     engine = pyttsx3.init()  # Initializing Text to Speech engine
#     voice = engine.getProperty('voices')
#     engine.setProperty('voice', voice[1].id)  # Selecting the voice
#     rate = engine.getProperty('rate')
#     engine.setProperty('rate', 150)  # Adjusting the speed of speech
#     engine.say(x)  # Saying the text
#     engine.runAndWait()  # Running the text to speech conversion

# if __name__ == "__main__":
#     while True:
#         if "hey assistant" in sptext().lower():
#             from GreetMe import greetMe
#             greetMe()

#             while True:
#                 data1 = sptext().lower()

#                 if "your name" in data1:
#                     name = " my name is assistant"
#                     speechtx(name)
#                 elif "old are you" in data1:
#                     age = "I'm a simple AI assistant, I don't have a real age."
#                     speechtx(age)
#                 elif "how are you" in data1 or "how r u" in data1:
#                     how = "I'm doing well, thank you for asking."
#                     speechtx(how)
#                 elif "what's the weather like" in data1:
#                     weather = "I'm unable to provide real-time weather information."
#                     speechtx(weather)
#                 elif "time" in data1:
#                     current_time = datetime.datetime.now().strftime("%H:%M:%p")
#                     speechtx(current_time)
#                 elif "youtube" in data1:
#                     webbrowser.open("https://www.youtube.com")
#                 elif "google" in data1:
#                     webbrowser.open("https://www.google.com")
#                 elif "joke" in data1:
#                     joke = pyjokes.get_joke(language="en", category="neutral")
#                     print(joke)
#                     speechtx(joke)
#                 elif 'play song' in data1:
#                     add = "D:\\MyProjects\\Voice Assistance\\Songs"
#                     listsong = os.listdir(add)
#                     print(listsong)
#                     os.startfile(os.path.join(add, listsong[0]))
#                 elif "bye" in data1:
#                     speechtx("Thank you for using my AI Assistant. Goodbye!")
#                     break  # This breaks out of the inner loop

#                 time.sleep(4)
#         else:
#             print("Please say 'hey assistant' to start.")

# import pyttsx3  # Text to speech Convert
# import speech_recognition as sr
# import webbrowser
# import datetime
# import pyjokes
# import os
# import time

# def sptext():  # Function Speech Recognition
#     recognizer = sr.Recognizer()  # Recognizer class for Speech Recognition
#     with sr.Microphone() as source:  # Microphone
#         print("Listening...")
#         recognizer.adjust_for_ambient_noise(source)  # for noise correction
#         audio = recognizer.listen(source)  # Listen to the audio from the microphone
#         try:
#             print("Recognizing...")
#             data = recognizer.recognize_google(audio)  # Recognize
#             print("You said: " + data)
#             return data
#         except sr.UnknownValueError:
#             print("Unable to recognize")
#             return "None"

# def speechtx(x):  # Function Text to Speech
#     engine = pyttsx3.init()  # Initializing Text to Speech engine
#     voice = engine.getProperty('voices')
#     engine.setProperty('voice', voice[1].id)  # Selecting the voice
#     rate = engine.getProperty('rate')
#     engine.setProperty('rate', 150)  # Adjusting the speed of speech
#     engine.say(x)  # Saying the text
#     engine.runAndWait()  # Running the text to speech conversion

# if __name__ == "__main__":
#     while True:
#         # Start listening for the activation phrase
#         if "hey assistant" in sptext().lower():
#             from GreetMe import greetMe
#             greetMe()

#             while True:
#                 data1 = sptext().lower()

#                 if "your name" in data1:
#                     name = "My name is assistant."
#                     speechtx(name)
#                 elif "old are you" in data1:
#                     age = "I'm a simple AI assistant; I don't have a real age."
#                     speechtx(age)
#                 elif "how are you" in data1 or "how r u" in data1:
#                     how = "I'm doing well, thank you for asking."
#                     speechtx(how)
#                 elif "what's the weather like" in data1:
#                     weather = "I'm unable to provide real-time weather information."
#                     speechtx(weather)
#                 elif "time" in data1:
#                     current_time = datetime.datetime.now().strftime("%H:%M:%p")
#                     speechtx(current_time)
#                 elif "youtube" in data1:
#                     webbrowser.open("https://www.youtube.com")
#                 elif "google" in data1:
#                     webbrowser.open("https://www.google.com")
#                 elif "joke" in data1:
#                     joke = pyjokes.get_joke(language="en", category="neutral")
#                     print(joke)
#                     speechtx(joke)
#                 elif 'play song' in data1:
#                     add = "D:\\MyProjects\\Voice Assistance\\Songs"
#                     listsong = os.listdir(add)
#                     print(listsong)
#                     os.startfile(os.path.join(add, listsong[0]))
#                 elif "bye" in data1:
#                     speechtx("Thank you for using my AI Assistant. Goodbye!")
#                     exit()  # Exit the program

#                 time.sleep(4)
#         else:
#             print("Please say 'hey assistant' to start.")

import pyttsx3  # Text to speech Convert
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time

def sptext():  # Function Speech Recognition
    recognizer = sr.Recognizer()  # Recognizer class for Speech Recognition
    with sr.Microphone() as source:  # Microphone
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # for noise correction
        audio = recognizer.listen(source)  # Listen to the audio from the microphone
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)  # Recognize
            print("You said: " + data)
            return data.lower()  # Return lowercase for easier comparison
        except sr.UnknownValueError:
            print("Unable to recognize")
            return "none"

def speechtx(x):  # Function Text to Speech
    engine = pyttsx3.init()  # Initializing Text to Speech engine
    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[1].id)  # Selecting the voice
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)  # Adjusting the speed of speech
    engine.say(x)  # Saying the text
    engine.runAndWait()  # Running the text to speech conversion

if __name__ == "__main__":
    while True:
        # Start listening for the activation phrase
        if "hey assistant" in sptext():
            from GreetMe import greetMe
            greetMe()

            while True:
                data1 = sptext()

                if "your name" in data1:
                    name = "My name is assistant."
                    speechtx(name)
                elif "old are you" in data1:
                    age = "I'm a simple AI assistant; I don't have a real age."
                    speechtx(age)
                elif "how are you" in data1 or "how r u" in data1:
                    how = "I'm doing well, thank you for asking."
                    speechtx(how)
                elif "what's the weather like" in data1:
                    weather = "I'm unable to provide real-time weather information."
                    speechtx(weather)
                elif "time" in data1:
                    current_time = datetime.datetime.now().strftime("%H:%M:%p")
                    speechtx(current_time)
                elif "youtube" in data1:
                    webbrowser.open("https://www.youtube.com")
                elif "google" in data1:
                    webbrowser.open("https://www.google.com")
                elif "joke" in data1:
                    joke = pyjokes.get_joke(language="en", category="neutral")
                    print(joke)
                    speechtx(joke)
                elif 'play song' in data1:
                    add = "D:\\MyProjects\\Voice Assistance\\Songs"
                    listsong = os.listdir(add)
                    print(listsong)
                    os.startfile(os.path.join(add, listsong[0]))
                elif "bye" in data1:
                    speechtx("Thank you for using my AI Assistant. Goodbye!")
                    exit()  # Exit the program

                time.sleep(4)
        else:
            print("Please say 'hey assistant' to start.")
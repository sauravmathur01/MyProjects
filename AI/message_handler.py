# message_handler.py
import datetime
import pyjokes
import webbrowser

def handle_message(user_message, speechtx):
    response_message = ""

    if "your name" in user_message:
        response_message = "My name is Zax, What can I help you?"
    elif "who are you" in user_message:
        response_message = "I'm an AI assistant, and I don't have personal experiences or feelings."
    elif "Tum Pagal Ho" in user_message:
        response_message = "Tum Ho."
    elif "who is Bihari" in user_message:
        response_message = "Sourabh is Bihari."
    elif "hey" in user_message.lower():
        response_message = "Hey, What can I help you?"
    elif "who created you" in user_message:
        response_message = "I was created by a team of programmers and researchers. I'm a Language model, and I was created recently."
    elif "old are you" in user_message:
        response_message = "I'm a simple AI assistant; I don't have an age. I'm a Language model, and I was created recently."
    elif "how are you" in user_message:
        response_message = "I'm doing well, thank you for asking. What can I help you?"
    elif "joke" in user_message:
        response_message = pyjokes.get_joke(language="en", category="neutral")
    elif "time" in user_message:
        current_time = datetime.datetime.now().strftime("%H:%M:%p")
        response_message = f"The current time is {current_time}."
        speechtx(response_message)
        return response_message
    elif "teammates" in user_message:
        Team = "Our teams are Sourabhh, Sanskriti, Shubhiii, Ratnesh, Shivani, and of course me Zax."
        speechtx(Team)
    elif "morning" in user_message:
        morning = "Good morning! Have a great day!"
        speechtx(morning)
    elif "evening" in user_message:
        evening = "Good evening! Have a great day!"
        speechtx(evening)
    elif "night" in user_message:
        night = "Good night! Have a great day!"
        speechtx(night)
    elif "introduce" in user_message or "introduced yourself" in user_message:
        introduce = "I'm Zax, a simple AI assistant. Yo! What's up? I'm here to make your life easier."
        speechtx(introduce)
    elif "afternoon" in user_message:
        afternoon = "Good afternoon! Have a great day!"
        speechtx(afternoon)
    elif "YouTube" in user_message:
        response_message = "Opening YouTube"
        webbrowser.open("https://www.youtube.com")
    elif "Google" in user_message:
        response_message = "Opening Google"
        webbrowser.open("https://www.google.com")
    elif 'play song' in user_message:
        webbrowser.open("https://www.youtube.com/watch?v=8LZgzAZ2lpQ")
    # elif "PPT" in user_message:
    #     response_message = "Opening PPT"
    #     webbrowser.open('D:\MyProjects\AI\static\Introducing-Zax-Your-AI-Powered-Voice-Assistant (1).pptx')
    elif "turn off" in user_message:
        response_message = "Microphone turned off."
    elif "bye" in user_message:
        response_message = "Thank you for using my AI Assistant. Goodbye!"
    else:
        response_message = "I'm sorry, I didn't understand. Can you please say that again?"

    speechtx(response_message)
    return response_message
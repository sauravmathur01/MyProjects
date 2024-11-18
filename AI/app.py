from flask import Flask, request, jsonify, render_template
import pyttsx3 # covert text to speech
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
from message_handler import handle_message   # Import the new handler function

app = Flask(__name__)

def speechtx(x):
    engine = pyttsx3.init()
    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    engine.say(x)
    engine.runAndWait()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/message', methods=['POST'])
def message():
    user_message = request.json['message']
    response_message = handle_message(user_message, speechtx)  # Call the function
    return jsonify({'response': response_message})
if __name__ == '__main__':
      app.run(debug=True)
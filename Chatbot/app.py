from flask import Flask, request, jsonify, render_template, send_file
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
from gtts import gTTS
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load pre-trained GPT-2 model and tokenizer
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)
model.eval()

def generate_response(prompt, max_length=100, temperature=0.7, top_k=50):
    """
    Generate a response from the model based on the input prompt.
    """
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    with torch.no_grad():
        output = model.generate(
            input_ids,
            max_length=max_length,
            temperature=temperature,
            top_k=top_k,
            pad_token_id=tokenizer.eos_token_id,
            do_sample=True,
        )
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response

@app.route("/")
def home():
    """
    Serve the main HTML page.
    """
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    """
    Endpoint to handle chat requests.
    """
    data = request.json
    user_input = data.get("message")
    if not user_input:
        return jsonify({"error": "No message provided"}), 400
    
    response = generate_response(user_input)
    return jsonify({"response": response})

@app.route("/speak", methods=["POST"])
def speak():
    """
    Endpoint to convert text to speech.
    """
    data = request.json
    text = data.get("text")
    if not text:
        return jsonify({"error": "No text provided"}), 400
    
    # Convert text to speech
    tts = gTTS(text)
    tts.save("response.mp3")
    return send_file("response.mp3", mimetype="audio/mp3")

if __name__ == "__main__":
    app.run(debug=True)
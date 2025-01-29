document.getElementById("send-btn").addEventListener("click", sendMessage);
document.getElementById("mic-btn").addEventListener("click", startVoiceInput);
document.getElementById("speak-btn").addEventListener("click", speakResponse);

let recognition;

function sendMessage() {
    const userInput = document.getElementById("user-input").value;
    if (!userInput) return;

    appendMessage("You", userInput);

    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ message: userInput }),
    })
        .then((response) => response.json())
        .then((data) => {
            appendMessage("Chatbot", data.response);
        })
        .catch((error) => {
            console.error("Error:", error);
        });

    document.getElementById("user-input").value = "";
}

function appendMessage(sender, message) {
    const chatBox = document.getElementById("chat-box");
    const messageElement = document.createElement("div");
    messageElement.innerHTML = `<strong>${sender}:</strong> ${message}`;
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function startVoiceInput() {
    if (!("webkitSpeechRecognition" in window)) {
        alert("Your browser does not support voice input.");
        return;
    }

    recognition = new webkitSpeechRecognition();
    recognition.continuous = false;
    recognition.interimResults = false;

    recognition.onresult = (event) => {
        const transcript = event.results[0][0].transcript;
        document.getElementById("user-input").value = transcript;
        sendMessage();
    };

    recognition.start();
}

function speakResponse() {
    const lastMessage = document.querySelector("#chat-box div:last-child");
    if (!lastMessage || !lastMessage.textContent.includes("Chatbot")) {
        alert("No chatbot response to speak.");
        return;
    }

    const text = lastMessage.textContent.replace("Chatbot:", "").trim();

    fetch("/speak", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ text: text }),
    })
        .then((response) => response.blob())
        .then((blob) => {
            const audioUrl = URL.createObjectURL(blob);
            const audio = new Audio(audioUrl);
            audio.play();
        })
        .catch((error) => {
            console.error("Error:", error);
        });
}

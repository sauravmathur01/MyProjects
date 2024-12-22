const startButton = document.getElementById('start-button');  // start button element for navigation , start button variable makes this line
const stopButton = document.getElementById('stop-button'); // Reference to the stop button
const messageList = document.getElementById('message-list');
const sendButton = document.getElementById('send-button');
const userInput = document.getElementById('user-input');
const micIcon = document.getElementById('mic-icon');
const hour = document.getElementById("hour");
const minute = document.getElementById("minute");
const week = document.querySelector(".week");


startButton.addEventListener('click', () => {
    startListening();
});

stopButton.addEventListener('click', () => {
    stopListening(); // Call the function to stop listening
});

sendButton.addEventListener('click', () => {
    const userMessage = userInput.value;
    if (userMessage) {
        displayMessage("YOU: " + userMessage);
        sendMessage(userMessage);
        userInput.value = ""; // Clear the input
    }
});

document.getElementById('mic-icon').addEventListener('click', () => {
    if (stopButton.style.display === "none") {
        startListening(); // Start listening if microphone is off
    } else {
        stopListening(); // Stop listening if microphone is on
    }
});

let recognition; // Declare recognition variable in a broader scope

function startListening() {
    recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.lang = 'en-US';
    recognition.interimResults = false; // Set to false to get only final results
    recognition.continuous = true; // Enable continuous listening

    recognition.start();
    startButton.style.display = "none"; // Hide start button
    stopButton.style.display = "inline"; // Show stop button

    // // Change the microphone icon to indicate it's active
    document.getElementById('mic-icon').classList.remove('fa-microphone-slash');
    document.getElementById('mic-icon').classList.add('fa-microphone');

    recognition.onresult = function(event) {
        const userMessage = event.results[event.results.length - 1][0].transcript;
        displayMessage("YOU: " + userMessage);
        sendMessage(userMessage);

        // Check if the user said "bye" to stop listening
        if (userMessage.toLowerCase().includes("bye")) {
            stopListening();
            displayMessage("Zax: Stopping listening. Goodbye!");
            console.log("Voice recognition stopped.");
        }
    };

    recognition.onend = function() {
        startButton.style.display = "inline"; // Show start button again when recognition ends
        stopButton.style.display = "none"; // Hide stop button

    //     // Change the microphone icon back to inactive
    document.getElementById('mic-icon').classList.remove('fa-microphone');
    document.getElementById('mic-icon').classList.add('fa-microphone-slash');

    };

    recognition.onerror = function(event) {
        console.error("Error occurred in recognition: " + event.error);
    };
}

function stopListening() {
    if (recognition) {
        recognition.stop(); // Stop the recognition
        startButton.style.display = "inline"; // Show start button
        stopButton.style.display = "none"; // Hide stop button

        // // Change the microphone icon back to inactive
        document.getElementById('mic-icon').classList.remove('fa-microphone');
        document.getElementById('mic-icon').classList.add('fa-microphone-slash');
        // Change the microphone icon back to inactive
        // micIcon.classList.remove('fa-microphone');
        // micIcon.classList.add('fa-microphone-slash');

    }
}

function sendMessage(message) {
    fetch('/api/message', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: message })
    })
    .then(response => response.json())
    .then(data => {
        displayMessage("ZAX: " + data.response);
    })
    .catch(error => console.error(error));
}

function displayMessage(message) {
    const messageElement = document.createElement('li');
    messageElement.textContent = message;
    messageList.appendChild(messageElement);
}
function updateClock() {
    const now = new Date();
    hour.textContent = String(now.getHours()).padStart(2, "0");
    minute.textContent = String(now.getMinutes()).padStart(2, "0");
  
    const dayIndex = now.getDay();
    Array.from(week.children).forEach((ele, index) => {
      ele.style.color = index === dayIndex ? "red" : "white";
    });
  }
  
  setInterval(updateClock, 1000);
  updateClock();
  function updateClock() {
    const now = new Date();
    hour.textContent = String(now.getHours()).padStart(2, "0");
    minute.textContent = String(now.getMinutes()).padStart(2, "0");

    const dayIndex = now.getDay();
    Array.from(week.children).forEach((ele, index) => {
        ele.style.color = index === dayIndex ? "red" : "white";
    });

    // Get the current date
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    const currentDate = now.toLocaleDateString(undefined, options);
    document.getElementById("current-date").textContent = currentDate; // Set the date
}
const userInputs = document.getElementById('user-input');
const suggestionsContainer = document.getElementById('suggestions-container');

const suggestions = [
    "hello",
    "how are you?",
    "what is your name?",
    "tell me a joke",
    "goodbye",
    "joke",
    "how are you",
    "Google",
    "YouTube"

];

userInputs.addEventListener('input', function() {
    const inputValue = this.value.toLowerCase();
    suggestionsContainer.innerHTML = ''; // Clear previous suggestions
    if (inputValue) {
        const filteredSuggestions = suggestions.filter(suggestion => 
            suggestion.toLowerCase().includes(inputValue)
        );

        filteredSuggestions.forEach(suggestion => {
            const suggestionItem = document.createElement('div');
            suggestionItem.classList.add('suggestion-item');
            suggestionItem.textContent = suggestion;
            suggestionItem.addEventListener('click', function() {
                userInput.value = suggestion; // Set input value to clicked suggestion
                suggestionsContainer.innerHTML = ''; // Clear suggestions
            });
            suggestionsContainer.appendChild(suggestionItem);
        });

        if (filteredSuggestions.length > 0) {
            suggestionsContainer.style.display = 'block'; // Show suggestions
        } else {
            suggestionsContainer.style.display = 'none'; // Hide if no suggestions
        }
    } else {
        suggestionsContainer.style.display = 'none'; // Hide if input is empty
    }
});

// Hide suggestions when clicking outside
document.addEventListener('click', function(event) {
    if (!userInput.contains(event.target)) {
        suggestionsContainer.style.display = 'none';
    }
});
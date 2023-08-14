const chatMessages = document.getElementById('chat-messages');
const userInput = document.getElementById('user-input');
const sendButton = document.getElementById('send-button');

sendButton.addEventListener('click', sendMessage);
userInput.addEventListener('keydown', (event) => {
    if (event.key === 'Enter') {
        sendMessage();
    }
});

function sendMessage() {
    const userMessage = userInput.value.trim();
    if (userMessage !== '') {
        appendMessage(userMessage, 'user-message');
        userInput.value = '';
        scrollToBottom();
        getChatbotResponse(userMessage);
    }
}

function getChatbotResponse(userMessage) {
    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: userMessage })
    })
    .then(response => response.json())
    .then(data => {
        const chatbotResponse = data.response;
        appendMessage(chatbotResponse, 'chatbot-message');
        scrollToBottom();
    })
    .catch(error => {
        console.error('Error fetching chatbot response:', error);
    });
}

function appendMessage(message, className) {
    const messageElement = document.createElement('div');
    messageElement.textContent = message;
    messageElement.classList.add(className);
    chatMessages.appendChild(messageElement);
}

function scrollToBottom() {
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

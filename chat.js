class ChatBot {
    constructor() {
        this.chatBox = document.getElementById('chatBox');
        this.chatForm = document.getElementById('chatForm');
        this.userInput = document.getElementById('userInput');
        this.messageContext = [];
        this.init();
    }

    init() {
        this.chatForm.addEventListener('submit', (e) => {
            e.preventDefault();
            this.handleUserInput();
        });
        this.addBotMessage("Olá! Sou um assistente AI especializado em soluções de chatbot para empresas. Como posso ajudar você hoje?");
    }

    addMessage(message, isBot) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${isBot ? 'bot-message' : 'user-message'}`;
        messageDiv.textContent = message;
        this.chatBox.appendChild(messageDiv);
        this.chatBox.scrollTop = this.chatBox.scrollHeight;
    }

    showTypingIndicator() {
        const indicator = document.createElement('div');
        indicator.className = 'typing-indicator';
        indicator.innerHTML = '<span></span><span></span><span></span>';
        this.chatBox.appendChild(indicator);
        this.chatBox.scrollTop = this.chatBox.scrollHeight;
        return indicator;
    }

    async handleUserInput() {
        const message = this.userInput.value.trim();
        if (!message) return;

        this.addMessage(message, false);
        this.userInput.value = '';
        const typingIndicator = this.showTypingIndicator();

        try {
            const response = await this.sendMessageToServer(message);
            this.chatBox.removeChild(typingIndicator);
            this.addBotMessage(response);
        } catch (error) {
            this.chatBox.removeChild(typingIndicator);
            this.addBotMessage("Desculpe, ocorreu um erro. Por favor, tente novamente.");
            console.error('Error:', error);
        }
    }

    async sendMessageToServer(message) {
        const response = await fetch('/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                message,
                context: this.messageContext
            }),
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        this.messageContext.push(
            { role: "user", content: message },
            { role: "assistant", content: data.response }
        );

        // Keep context window manageable
        if (this.messageContext.length > 10) {
            this.messageContext = this.messageContext.slice(-10);
        }

        return data.response;
    }

    addBotMessage(message) {
        this.addMessage(message, true);
    }
}

// Initialize chatbot when page loads
window.addEventListener('load', () => {
    new ChatBot();
});
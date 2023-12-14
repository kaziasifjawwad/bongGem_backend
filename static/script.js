function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    const chatBox = document.getElementById('chat-box');
    chatBox.innerHTML += '<div class="user-message">' + userInput + '</div>';

            // Clear user input field
            document.getElementById('user-input').value = '';

            // Send user message to Flask server
            fetch('/get_response', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ message: userInput })
            })
            .then(response => response.json())
            .then(data => {
                // Append bot response to chat box
                chatBox.innerHTML += '<div class="bot-message">' + data.message + '</div>';
                console.log("hello");
            });
        }
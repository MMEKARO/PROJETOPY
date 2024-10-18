async function sendMessage() {
    const userInput = document.getElementById("user-input").value;
    const chatBox = document.getElementById("chat-box");

    // Adicionar a mensagem do usuário na interface
    chatBox.innerHTML += `<p><strong>Você:</strong> ${userInput}</p>`;
    document.getElementById("user-input").value = '';

    // Enviar a mensagem para o backend
    const response = await fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ input: userInput })
    });

    const data = await response.json();
    chatBox.innerHTML += `<p><strong>Assistente:</strong> ${data.message}</p>`;
}

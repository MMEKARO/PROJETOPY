import os
from flask import Flask, request, render_template, jsonify
from groq import Groq
from dotenv import load_dotenv

# Carregar variáveis de ambiente do .env
load_dotenv()

# Configurar a API Key
API_KEY = os.getenv("GROQ_API_KEY")
if not API_KEY:
    raise ValueError("A chave da API não foi encontrada. Verifique o arquivo .env.")

# Inicializar o cliente Groq
client = Groq(api_key=API_KEY)

# Inicializar o Flask
app = Flask(__name__)

# Rota para a interface
@app.route('/')
def home():
    return render_template('index.html')

# Rota para o chat
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['input']
    messages = [{"role": "user", "content": user_input}]
    
    # Chamada para a API com as mensagens
    response = client.chat.completions.create(
        messages=messages,
        model="gemma2-9b-it"
    )
    
    assistant_response = response['choices'][0]['message']['content']
    return jsonify({'message': assistant_response})

# Executar o servidor
if __name__ == '__main__':
    app.run(debug=True)

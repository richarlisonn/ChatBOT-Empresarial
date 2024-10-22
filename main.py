import openai
import os

# (COLA COMANDO)]

# (/COLA COMANDO)]

def enviar_mensagem(mensagem, lista_mensagens=[]):
    # Adiciona a mensagem do usuário à lista
    lista_mensagens.append({"role": "user", "content": mensagem})

    try:
        # Envia a mensagem para a API do OpenAI e obtém a resposta
        resposta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0125",
            messages=lista_mensagens,
        )

        # Adiciona a resposta do modelo à lista de mensagens
        lista_mensagens.append(resposta["choices"][0]["message"])

        # Retorna a resposta para exibição
        return resposta["choices"][0]["message"]

    except Exception as e:
        # Tratamento de exceções, por exemplo, problemas de conexão ou falhas de autenticação
        print(f"Erro ao enviar mensagem: {e}")
        return {"content": "Desculpe, houve um erro ao processar a sua solicitação."}

# Loop principal do chatbot
lista_mensagens = []
while True:
    # Recebe a mensagem do usuário
    texto = input("Escreva aqui sua mensagem:")

    if texto.lower() == "sair":
        break
    else:
        # Envia a mensagem para o chatbot e imprime a resposta
        resposta = enviar_mensagem(texto, lista_mensagens)
        print("Chatbot:", resposta["content"])
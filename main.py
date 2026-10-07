from ollama import chat

messages = []

while True:
    Bond = input("Write your message here : ")
    if Bond == "STOP":
        break

    messages.append({'role': 'user', 'content': Bond})
    response = chat(
        model='llama3.2',
        messages=messages,
    )
    messages.append({'role': 'assistant', 'content': response.message.content})
    print(response.message.content)

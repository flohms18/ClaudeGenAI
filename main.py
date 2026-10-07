from ollama import chat
from fastapi.responses import HTMLResponse
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get('/')
async def root():
    return {
        "msg" : "Hello World"
    }

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

import os
from openai import OpenAI

client = OpenAI(api_key="ADD_YOUR_API_KEY")

print("chat completion Model")
messages = []

while True:
    user_input = input("you: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting chat.")
        break
    messages.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(model="gpt-4.1-mini", messages=messages)
    reply = response.choices[0].message.content
    print("AI: " + reply)
    messages.append({"role": "assistant", "content": reply})

print("Chat session ended.")

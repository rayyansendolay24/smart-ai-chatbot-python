import os
from dotenv import load_dotenv
from groq import Groq

from memory import add_message, get_history
from config import SYSTEM_PROMPT

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

print("Smart AI Chatbot Started")
print("Type 'exit' to stop\n")

add_message("system", SYSTEM_PROMPT)

while True:

    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Bot: Goodbye!")
        break

    add_message("user", user_input)

    response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=get_history()
)

    reply = response.choices[0].message.content

    print("Bot:", reply)

    add_message("assistant", reply)
# Smart AI Chatbot (Python)

## Project Overview

Smart AI Chatbot is a Python-based conversational assistant that generates intelligent responses using a Large Language Model (LLM). The chatbot maintains conversation history so it can provide context-aware replies and simulate natural interaction.

This project demonstrates the integration of AI APIs with Python to build a simple but functional chatbot system.

---

## Features

* AI-generated responses using the LLaMA language model
* Maintains conversation history
* Modular Python architecture
* Secure API key handling using environment variables
* Interactive command-line interface

---

## Technologies Used

* Python
* Groq API
* LLaMA 3.1 Model
* python-dotenv

---

## Project Structure

AI_Chatbot_Project

├── chatbot.py        # Main chatbot engine
├── config.py         # Chatbot personality configuration
├── memory.py         # Conversation memory management
├── .env              # API key storage (not uploaded to GitHub)
├── requirements.txt  # Python dependencies
└── README.md         # Project documentation

---

## Installation

Clone the repository

git clone https://github.com/yourusername/smart-ai-chatbot-python.git

Navigate to the project directory

cd smart-ai-chatbot-python

Create a virtual environment

python -m venv venv

Activate the environment

Windows:

venv\Scripts\activate

Install required libraries

pip install -r requirements.txt

---

## API Setup

Create a `.env` file in the project directory and add your API key:

GROQ_API_KEY=your_api_key_here

You can obtain a free API key from the Groq developer console.

---

## Running the Chatbot

Run the chatbot using the command:

python chatbot.py

Example interaction:

You: Hello
Bot: Hello. How can I assist you today?

You: What is artificial intelligence?
Bot: Artificial intelligence is a branch of computer science that focuses on building systems capable of performing tasks that normally require human intelligence.

---

## Future Improvements

* Voice assistant integration
* Graphical chatbot interface
* Internet search capability
* Persistent memory using a database
* Wake-word activation

---

## Author

Rayyan Sendolay

---

## License

This project is developed for educational and learning purposes.

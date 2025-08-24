# Groq Chatbot

A web-based AI chatbot using **Groq LLaMA models** with a **React frontend** and **Flask backend**. This project demonstrates how to integrate a powerful language model into a web application for interactive conversations.

---

## Features

- **AI-powered chat:** Uses Groq's LLaMA 3.3 model to respond to user queries.
- **Conversation history:** Maintains conversation context for more coherent responses.
- **React frontend:** Interactive, responsive chat interface.
- **Flask backend:** Handles API requests and interacts with the Groq model.
- **CORS support:** Allows the frontend to access the backend securely.
- **Deployable:** React build is served through Flask for production-ready deployment.

---

## Project Structure

Chatbot/
│
├─ backend/
│ ├─ app.py # Flask backend
│ └─ ... # Other backend files
│
├─ frontend/
│ ├─ src/
│ │ ├─ App.js # React main component
│ │ └─ ... # Other frontend components
│ ├─ public/
│ │ └─ index.html # React HTML template
│ └─ package.json # React project config
│
└─ README.md



---

## Installation

### Backend (Flask)
1. Create and activate a Python virtual environment:
```bash
python -m venv venv
venv\Scripts\activate      # Windows
# or
source venv/bin/activate   # Mac/Linux

pip install flask flask-cors groq
python backend/app.py



cd frontend
npm install
npm start
npm run build


Configuration

API Key: Update the Groq API key in backend/app.py:

client = Groq(api_key="YOUR_GROQ_API_KEY")


Model: You can change the model in app.py:

model="llama-3.3-70b-versatile"


Acknowledgements

Groq AI
 for providing the LLaMA API.

React
 and Flask
 for frontend and backend frameworks.

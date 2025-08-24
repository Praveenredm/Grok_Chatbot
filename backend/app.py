# # # from groq import Groq

# # # # Initialize client with your Groq key
# # # client = Groq(api_key="gsk**************************")

# # # def chat_with_groq(prompt):
# # #     response = client.chat.completions.create(
# # #         model="llama-3.3-70b-versatile",  # Updated model
# # #         messages=[{"role": "user", "content": prompt}]
# # #     )
# # #     return response.choices[0].message.content.strip()

# # # if __name__ == "__main__":
# # #     while True:
# # #         user_input = input("You: ")
# # #         if user_input.lower() in ["quit", "exit", "bye"]:
# # #             break
# # #         response = chat_with_groq(user_input)
# # #         print("Chatbot:", response)










# # # #API_KEY ="***********************"







# # from groq import Groq
# # import os

# # # Initialize Groq client
# # API_KEY = os.getenv("****************************")  # store your key in an environment variable
# # client = Groq(api_key=API_KEY)

# # def chat_with_groq(messages):
# #     """
# #     messages: list of dictionaries like [{"role": "user", "content": "..."}]
# #     """
# #     try:
# #         response = client.chat.completions.create(
# #             model="llama-3.3-70b-versatile",
# #             messages=messages
# #         )
# #         return response.choices[0].message.content.strip()
# #     except Exception as e:
# #         return f"Error: {e}"

# # if __name__ == "__main__":
# #     conversation_history = []  # this will store the full chat history

# #     print("Chatbot is ready! Type 'quit' to exit.")

# #     while True:
# #         user_input = input("You: ")
# #         if user_input.lower() in ["quit", "exit", "bye"]:
# #             break

# #         # Add user's message to history
# #         conversation_history.append({"role": "user", "content": user_input})

# #         # Get chatbot response
# #         assistant_reply = chat_with_groq(conversation_history)

# #         # Add assistant's reply to history
# #         conversation_history.append({"role": "assistant", "content": assistant_reply})

# #         print("Chatbot:", assistant_reply)











# from flask import Flask, request, jsonify
# from groq import Groq
# import os

# app = Flask(__name__)
# client = Groq(api_key=os.getenv("gs*****************************************"))

# conversation_history = []

# @app.route("/chat", methods=["POST"])
# def chat():
#     global conversation_history
#     user_input = request.json.get("message")
#     conversation_history.append({"role": "user", "content": user_input})

#     response = client.chat.completions.create(
#         model="llama-3.3-70b-versatile",
#         messages=conversation_history
#     )

#     reply = response.choices[0].message.content.strip()
#     conversation_history.append({"role": "assistant", "content": reply})

#     return jsonify({"reply": reply})

# if __name__ == "__main__":
#     app.run(debug=True)










# backend/app.py
from flask import Flask, request, jsonify, send_from_directory
from groq import Groq
import os
from flask_cors import CORS  # allows React frontend to access backend

app = Flask(__name__, static_folder="../frontend/build", static_url_path="/")
CORS(app)  # enable CORS for all routes

# Initialize Groq client
client = Groq(api_key="gsk_*************************************v")

conversation_history = []

# Serve React frontend
@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

# Chat API
@app.route("/chat", methods=["POST"])
def chat():
    global conversation_history
    user_input = request.json.get("message")
    conversation_history.append({"role": "user", "content": user_input})

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=conversation_history
        )
        reply = response.choices[0].message.content.strip()
    except Exception as e:
        reply = f"Error: {e}"

    conversation_history.append({"role": "assistant", "content": reply})
    return jsonify({"reply": reply})

# Fallback for React Router
@app.errorhandler(404)
def not_found(e):
    return send_from_directory(app.static_folder, "index.html")

if __name__ == "__main__":
    app.run(debug=True)

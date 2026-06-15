import os
from google import genai

client = genai.Client(api_key="AQ.Ab8RN6JtIDlz4V_VtIcNGhxCPWNOGaXQ2CbhJhzRFQfNLp-hmQ")

chat = client.chats.create(model="gemini-3.5-flash")

print("Gemini Chatbot Initialized! Type 'quit' to exit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit"]:
        print("Goodbye!")
        break
        
    if not user_input.strip():
        continue

    response = chat.send_message(user_input)
    print(f"\nGemini: {response.text}\n")

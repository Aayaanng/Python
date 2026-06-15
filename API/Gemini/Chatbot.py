import os
from google import genai

# Initialize the client directly with your API key string
client = genai.Client(api_key="AQ.Ab8RN6JtIDlz4V_VtIcNGhxCPWNOGaXQ2CbhJhzRFQfNLp-hmQ")

# Start an interactive chat session with history tracking
chat = client.chats.create(model="gemini-3.5-flash")

print("Gemini Chatbot Initialized! Type 'quit' to exit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit"]:
        print("Goodbye!")
        break
        
    if not user_input.strip():
        continue

    # Send message to the session; history updates automatically
    response = chat.send_message(user_input)
    print(f"\nGemini: {response.text}\n")

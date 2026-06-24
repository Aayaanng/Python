import os
from dotenv import load_dotenv
from google import genai

# 1. Load the API key from your local .env file FIRST
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# 2. Check if the key was found to prevent empty crashes
if not api_key:
    raise ValueError("Error: GOOGLE_API_KEY not found in your .env file!")

# 3. Pass the valid environment variable directly into the GenAI client
client = genai.Client(api_key=api_key)

# 4. Initialize the chat session using a standard production model
chat = client.chats.create(model="gemini-3.5-flash")

print("Gemini Chatbot Initialized! Type 'quit' or 'exit' to end the session.\n")

while True:
    user_input = input("You: ")
    
    if user_input.lower() in ["quit", "exit"]:
        print("Goodbye!")
        break
        
    if not user_input.strip():
        continue
        
    try:
        # 5. Send message and catch API errors gracefully
        response = chat.send_message(user_input)
        print(f"\nGemini: {response.text}\n")
    except Exception as e:
        print(f"\nAPI Error: {e}\n")

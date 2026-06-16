import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load API key from .env file
load_dotenv()

# Create the LLM (AI model) object
llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Test it
response = llm.invoke("What is LangChain?")
print(response.content)
#prompt template
from langchain_core.prompts import PromptTemplate

# Define template with a {topic} placeholder
template = PromptTemplate(
    input_variables=["topic"],
    template="Write a short poem about {topic}."
)

# Fill in the placeholder
filled_prompt = template.format(topic="mountains")
print(filled_prompt)
# Output: "Write a short poem about mountains."

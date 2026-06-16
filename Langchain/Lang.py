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
from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful teacher who explains topics simply."),
    ("human", "Explain {concept} to a 10-year-old child.")
])

# Format with actual values
messages = chat_template.format_messages(concept="gravity")

response = llm.invoke(messages)
print(response.content)
#multiple variables in a template
template = PromptTemplate(
    input_variables=["language", "topic", "level"],
    template="Explain {topic} in {language} for a {level} student."
)

prompt = template.format(language="Hindi", topic="photosynthesis", level="class 8")
response = llm.invoke(prompt)
print(response.content)
#pipe operator ( | )
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

llm = ChatGoogleGenerativeAI(model='gemini-3.5-flash', )

# Step 1: Define prompt
prompt = PromptTemplate(
    input_variables=["country"],
    template="What is the capital city of {country}?"
)

# Step 2: Build the chain
chain = prompt | llm | StrOutputParser()

# Step 3: Run the chain
result = chain.invoke({"country": "France"})
print(result)  # Output: Paris
#Two-Step Sequential Chain
# Chain 1: Generate a story
story_prompt = PromptTemplate(
    input_variables=["genre"],
    template="Write a 3-sentence {genre} story."
)
story_chain = story_prompt | llm | StrOutputParser()

# Chain 2: Summarise the story
summary_prompt = PromptTemplate(
    input_variables=["story"],
    template="Summarise this story in one sentence: {story}"
)
summary_chain = summary_prompt | llm | StrOutputParser()

# Run Chain 1
story = story_chain.invoke({"genre": "adventure"})
print('Story:', story)

# Pass output of Chain 1 into Chain 2
summary = summary_chain.invoke({"story": story})
print('Summary:', summary)
#RunnableSequence — Fully Automated Pipeline
from langchain_core.runnables import RunnablePassthrough

# Full pipeline: input → story → summary
full_chain = (
    story_chain
    | (lambda story: {'story': story})
    | summary_chain
)

final_result = full_chain.invoke({"genre": "mystery"})
print(final_result)

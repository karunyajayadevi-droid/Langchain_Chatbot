
import pandas as pd
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

# Connect to Ollama
model = ChatOllama(
    model="llama3.2",
    temperature=0.7
)

# Create five prompt templates
templates = {
    "General Assistant":
        "You are a helpful college assistant. Answer clearly: {user_input}",

    "Study Assistant":
        "You are a friendly study assistant. Explain in simple English with examples: {user_input}",

    "Programming Assistant":
        "You are a programming tutor. Explain step by step with an example: {user_input}",

    "Exam Assistant":
        "You are an exam preparation assistant. Give a structured answer with headings and important points: {user_input}",

    "College Information":
        "You are a college information assistant. Answer this college-related query clearly: {user_input}"
}

# Test each prompt template
for name, template_text in templates.items():

    print("\n------------------------------")
    print("Template:", name)
    print("------------------------------")

    prompt = ChatPromptTemplate.from_template(template_text)

    # Build LangChain chain
    chain = prompt | model

    # Dynamic user input
    result = chain.invoke({
        "user_input": "What is Artificial Intelligence?"
    })

    print(result.content)

print("\nAll five prompt templates executed successfully!")

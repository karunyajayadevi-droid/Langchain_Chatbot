
import pandas as pd
from datetime import datetime

from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

# Connect to Ollama
model = ChatOllama(
    model="llama3.2",
    temperature=0.7
)

# Read 20 user queries
queries = pd.read_csv("dataset/user_queries.csv")

# Prompt templates
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

responses = []

print("Starting 20 Query Tests...\n")

# Process each query
for index, row in queries.iterrows():

    template_name = row["template_name"]
    user_query = row["user_query"]

    print(f"Processing Query {index + 1}/20")
    print("Question:", user_query)

    prompt = ChatPromptTemplate.from_template(
        templates[template_name]
    )

    chain = prompt | model

    result = chain.invoke({
        "user_input": user_query
    })

    answer = result.content

    print("Response:", answer)
    print("-" * 50)

    responses.append({
        "query_id": row["query_id"],
        "template_name": template_name,
        "user_query": user_query,
        "chatbot_response": answer,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

# Save all responses
df = pd.DataFrame(responses)

df.to_csv(
    "dataset/chatbot_responses.csv",
    index=False
)

print("\nAll 20 queries processed successfully!")
print("Responses saved in dataset/chatbot_responses.csv")

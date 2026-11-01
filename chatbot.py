
import pandas as pd
from datetime import datetime
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

# Connect to Ollama
model = ChatOllama(
    model="llama3.2",
    temperature=0.7
)

# Five prompt templates
templates = {
    "1": (
        "General Assistant",
        "You are a helpful college assistant. "
        "Answer clearly: {user_input}"
    ),

    "2": (
        "Study Assistant",
        "You are a friendly study assistant. "
        "Explain in simple English with examples: {user_input}"
    ),

    "3": (
        "Programming Assistant",
        "You are a programming tutor. "
        "Explain step by step with an example: {user_input}"
    ),

    "4": (
        "Exam Assistant",
        "You are an exam preparation assistant. "
        "Give a structured answer with headings and important points: {user_input}"
    ),

    "5": (
        "College Information",
        "You are a college information assistant. "
        "Answer this college-related query clearly: {user_input}"
    )
}

# Store chatbot responses
responses = []

print("\n===================================")
print("       COLLEGE ASSISTANT CHATBOT")
print("===================================")

while True:

    print("\nChoose a prompt template:")
    print("1. General Assistant")
    print("2. Study Assistant")
    print("3. Programming Assistant")
    print("4. Exam Assistant")
    print("5. College Information")
    print("Type 'exit' to stop")

    choice = input("\nEnter your choice: ").strip()

    if choice.lower() == "exit":
        break

    if choice not in templates:
        print("Invalid choice. Please select 1 to 5.")
        continue

    template_name, template_text = templates[choice]

    user_input = input("\nEnter your question: ").strip()

    if not user_input:
        print("Please enter a question.")
        continue

    # Create prompt template
    prompt = ChatPromptTemplate.from_template(template_text)

    # Create LangChain chain
    chain = prompt | model

    print("\nGenerating response...")

    # Execute chain
    result = chain.invoke({
        "user_input": user_input
    })

    answer = result.content

    print("\nChatbot Response:")
    print(answer)

    # Save response
    responses.append({
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "template_name": template_name,
        "user_query": user_input,
        "chatbot_response": answer
    })

# Save responses to CSV
if responses:
    df = pd.DataFrame(responses)

    df.to_csv(
        "dataset/chatbot_responses.csv",
        index=False
    )

    print("\nChatbot responses saved successfully!")

print("\nThank you for using College Assistant Chatbot!")

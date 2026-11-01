
from langchain_ollama import ChatOllama

# Connect to the local Ollama model
model = ChatOllama(
    model="llama3.2",
    temperature=0.7
)

# Test the model
response = model.invoke("What is Artificial Intelligence?")

print("LangChain Response:")
print(response.content)

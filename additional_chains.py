
import pandas as pd
from datetime import datetime

from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

# Connect to Ollama
model = ChatOllama(
    model="llama3.2",
    temperature=0.7
)

results = []

# --------------------------------
# CHAIN 1: SUMMARIZATION CHAIN
# --------------------------------

summary_prompt = ChatPromptTemplate.from_template(
    """
    You are a summarization assistant.

    Summarize the following text in simple English.
    Include only the important points.

    Text: {text}
    """
)

summary_chain = summary_prompt | model

sample_text = """
Artificial Intelligence is a technology that enables
machines to perform tasks that normally require human
intelligence. AI is used in education, healthcare,
business, transportation and many other fields.
It helps automate tasks, improve decision-making
and increase productivity.
"""

summary_result = summary_chain.invoke({
    "text": sample_text
})

print("\n========== SUMMARIZATION CHAIN ==========")
print(summary_result.content)

results.append({
    "chain_name": "Summarization Chain",
    "input": sample_text,
    "output": summary_result.content,
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
})


# --------------------------------
# CHAIN 2: QUESTION ANSWERING CHAIN
# --------------------------------

qa_prompt = ChatPromptTemplate.from_template(
    """
    You are a helpful question answering assistant.

    Answer the question using the given context.
    If the answer is not available in the context,
    clearly mention that.

    Context: {context}

    Question: {question}
    """
)

qa_chain = qa_prompt | model

context = """
LangChain is a framework used to develop applications
powered by large language models. It provides prompt
templates, chains and integrations with different
language models. It helps developers build modular
AI applications.
"""

question = "What is LangChain and what are its main features?"

qa_result = qa_chain.invoke({
    "context": context,
    "question": question
})

print("\n========== QUESTION ANSWERING CHAIN ==========")
print(qa_result.content)

results.append({
    "chain_name": "Question Answering Chain",
    "input": question,
    "output": qa_result.content,
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
})


# --------------------------------
# SAVE RESULTS TO CSV
# --------------------------------

df = pd.DataFrame(results)

df.to_csv(
    "dataset/chain_results.csv",
    index=False
)

print("\nChain results saved successfully!")

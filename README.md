# Week 10 – LangChain Basics

## Project Title
Building LLM Applications using LangChain Prompt Templates and Chains

## Introduction
This project demonstrates the development of a College Assistant Chatbot using LangChain and Ollama. It uses reusable prompt templates and LLM chains to generate responses to different user queries.

## Objectives
- Understand the fundamentals of LangChain.
- Create reusable prompt templates.
- Connect LangChain with a local Ollama model.
- Develop a College Assistant Chatbot.
- Build summarization and question-answering chains.
- Test the chatbot using 20 different queries.
- Save generated responses into CSV files.

## Technologies Used
- Python 3.13
- LangChain
- Ollama
- Llama 3.2
- Pandas
- Jupyter Notebook
- Visual Studio Code

## Project Features
1. Five different prompt templates.
2. Interactive College Assistant Chatbot.
3. Summarization Chain.
4. Question Answering Chain.
5. Testing with 20 user queries.
6. CSV storage of chatbot responses and chain results.

## Folder Structure
```text
LangChain_Basics/
├── dataset/
│   ├── prompts.csv
│   ├── user_queries.csv
│   ├── chatbot_responses.csv
│   └── chain_results.csv
├── notebook/
│   └── Week10_LangChain_Basics.ipynb
├── langchain_chatbot.py
├── additional_chains.py
├── batch_test.py
├── comparison.md
├── README.md
└── requirements.txt
```

## Execution Instructions

1. Install Ollama and download the Llama 3.2 model.
2. Install the required Python libraries.
3. Run `langchain_chatbot.py` to start the chatbot.
4. Run `additional_chains.py` to execute the additional chains.
5. Run `batch_test.py` to test 20 user queries.
6. Open the Jupyter Notebook to view the results.

## Output Files
- `prompts.csv`: Stores five prompt templates.
- `user_queries.csv`: Stores 20 user questions.
- `chatbot_responses.csv`: Stores generated chatbot responses.
- `chain_results.csv`: Stores summarization and question-answering results.

## Conclusion
The project successfully demonstrates how LangChain can be integrated with Ollama to develop modular LLM applications. Prompt templates and chains make chatbot development more organized and reusable. This project provides a foundation for future Retrieval-Augmented Generation (RAG) applications and vector database integration.
# Observations – Week 10 LangChain Basics

## 1. Accuracy
The chatbot generated responses to 20 different user queries. Most responses were relevant to the questions and provided useful information about artificial intelligence, programming and education. However, some answers may require verification.

## 2. Response Quality
The five prompt templates produced responses suited to different scenarios:
- General Assistant provided general information.
- Study Assistant explained academic concepts in simple English.
- Programming Assistant provided programming explanations.
- Exam Assistant generated structured answers.
- College Information provided student-related guidance.

## 3. Prompt Templates
Reusable prompt templates helped organize instructions and dynamically accept user input. Different templates produced different response styles.

## 4. Summarization Chain
The summarization chain successfully converted longer text into shorter summaries containing important points.

## 5. Question Answering Chain
The question-answering chain generated answers using the provided context and question.

## 6. CSV Storage
The generated user queries, chatbot responses, prompt templates and chain results were saved in CSV files using Pandas.

## 7. Comparison with Week 9
Week 9 used direct Python and Ollama integration to develop a basic chatbot. Week 10 introduced LangChain prompt templates and chains, making the application more modular and reusable.

## 8. Advantages
- Reusable prompt templates.
- Modular application development.
- Local LLM integration using Ollama.
- Multiple chatbot scenarios.
- Automated CSV storage.
- Support for different LLM tasks.

## 9. Limitations
- Responses may sometimes contain incorrect information.
- Generation speed depends on the local computer and model.
- The chatbot depends on the selected prompt and available context.
- The question-answering chain uses the context supplied to it.

## 10. Conclusion
The project helped me understand the fundamentals of LangChain, prompt templates and LLM chains. I successfully integrated LangChain with Ollama, developed a College Assistant Chatbot, created two additional chains and tested 20 different queries. This project provides a foundation for future RAG and vector database integration.
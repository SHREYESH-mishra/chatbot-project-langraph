# chatbot-project-langraph
AI-powered chatbot built with Streamlit, LangGraph, and LangChain featuring persistent multi-thread conversations, session-based memory, real-time response streaming, and an interactive chat interface. Demonstrates conversational AI, state management, and scalable LLM application development.
# 🤖 LangGraph AI Chatbot

An AI-powered conversational chatbot built with **Streamlit**, **LangGraph**, and **LangChain**. The application provides an interactive chat interface with persistent conversation memory, multi-thread chat management, and real-time streaming responses.

This project demonstrates how to build scalable conversational AI applications using LangGraph's state management and Streamlit's modern UI components.

---

## 🚀 Features

- 💬 Interactive chatbot interface
- ⚡ Real-time AI response streaming
- 🧠 Persistent conversation memory
- 🔄 Multiple chat sessions
- 📂 Conversation history management
- 🆕 Create unlimited new chats
- 🎯 Session-based state management
- 🖥️ Clean and responsive Streamlit UI

---

## 🛠️ Tech Stack

- Python
- Streamlit
- LangGraph
- LangChain
- LangChain Core
- UUID
- LLM (OpenAI/Groq/Ollama Compatible)

---

## 📂 Project Structure

```
langgraph-chatbot/
│
├── app.py                  # Streamlit frontend
├── langgraph_backend.py    # LangGraph backend
├── requirements.txt
├── README.md
└── assets/
```

---

## ⚙️ How It Works

1. User starts a new conversation.
2. A unique Thread ID is generated.
3. User messages are sent to the LangGraph backend.
4. LangGraph maintains conversation state and memory.
5. AI responses are streamed in real time.
6. Users can revisit previous conversations anytime.

---

## ✨ Key Features

### 🔹 Multi-Thread Conversations
Each chat session is assigned a unique UUID, allowing multiple independent conversations.

### 🔹 Persistent Memory
LangGraph stores conversation history, enabling users to continue previous chats seamlessly.

### 🔹 Streaming Responses
AI responses are streamed token-by-token for a smooth and interactive experience.

### 🔹 Session Management
- Create New Chat
- View Previous Conversations
- Switch Between Threads
- Maintain Chat History

---

## 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/langgraph-chatbot.git

cd langgraph-chatbot
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

---

## 📦 Requirements

```
streamlit
langgraph
langchain
langchain-core
```

Or install using:

```bash
pip install streamlit langgraph langchain langchain-core
```

---

## 🧠 Concepts Demonstrated

- Conversational AI
- LangGraph State Management
- LangChain Messages
- Streamlit Chat Components
- Session State Management
- UUID-based Thread Handling
- Real-time Streaming Responses
- Modular Backend Architecture

---

## 📸 Application Features

- AI Chat Interface
- Conversation Sidebar
- Multiple Chat Threads
- Persistent Chat History
- Streaming AI Responses
- Session-Based Memory

---

## 🔮 Future Enhancements

- User Authentication
- Database Integration (MongoDB/PostgreSQL)
- Chat Export (PDF/Markdown)
- File Upload Support
- Voice Chat
- Image Understanding
- Docker Containerization
- AWS Cloud Deployment
- Multi-Model Support

---

## 👨‍💻 Author

**Shreyesh Mishra**

Cloud | DevOps | AI/ML Enthusiast

---

## ⭐ Support

If you found this project useful, consider giving it a **⭐ Star** on GitHub.

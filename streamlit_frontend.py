import streamlit as st
from langgraph_backend import chatbot
from langchain_core.messages import HumanMessage
import uuid


def generate_thread_id():
    return str(uuid.uuid4())


def add_thread(thread_id):
    if thread_id not in st.session_state['chat_threads']:
        st.session_state['chat_threads'].append(thread_id)


def reset_chat():
    thread_id = generate_thread_id()
    st.session_state['thread_id'] = thread_id
    add_thread(thread_id)
    st.session_state['message_history'] = []


def load_conversation(thread_id):
    return chatbot.get_state(
        config={'configurable': {'thread_id': thread_id}}
    ).values['messages']


# ------------------ Session Init ------------------
if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = generate_thread_id()

if 'chat_threads' not in st.session_state:
    st.session_state['chat_threads'] = []

add_thread(st.session_state['thread_id'])

# ------------------ Sidebar ------------------
st.sidebar.title("LangGraph Chatbot")

if st.sidebar.button("New Chat"):
    reset_chat()

st.sidebar.header("My Conversations")

for tid in st.session_state['chat_threads'][::-1]:
    if st.sidebar.button(tid):
        st.session_state['thread_id'] = tid
        messages = load_conversation(tid)

        temp_messages = []
        for msg in messages:
            role = "user" if isinstance(msg, HumanMessage) else "assistant"
            temp_messages.append({
                "role": role,
                "content": msg.content
            })

        st.session_state['message_history'] = temp_messages

# ------------------ Chat UI ------------------
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

user_input = st.chat_input("Type here...")

if user_input:
    st.session_state['message_history'].append({
        'role': 'user',
        'content': user_input
    })

    with st.chat_message("user"):
        st.text(user_input)

    with st.chat_message("assistant"):
        CONFIG = {
            'configurable': {
                'thread_id': st.session_state['thread_id']
            }
        }

        ai_message = st.write_stream(
            chunk.content
            for chunk, _ in chatbot.stream(
                {'messages': [HumanMessage(content=user_input)]},
                config=CONFIG,
                stream_mode="messages"
            )
        )

    st.session_state['message_history'].append({
        'role': 'assistant',
        'content': ai_message
    })

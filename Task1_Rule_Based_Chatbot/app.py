import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Rule-Based Chatbot", page_icon="💬")
st.title("💬 Rule-Based Chatbot")
st.caption("A simple chatbot built with Python keyword matching and if/elif rules.")

def get_response(message: str) -> str:
    text = message.lower().strip()

    if any(word in text for word in ["hello", "hi", "hey", "good morning", "good evening"]):
        return "Hello! 👋 How can I help you today?"
    elif "your name" in text or "who are you" in text:
        return "I'm CodBot, a simple rule-based chatbot created for the CodSoft AI internship."
    elif "how are you" in text:
        return "I'm doing well, thanks for asking! How are you?"
    elif any(word in text for word in ["course", "courses", "learn"]):
        return "You can start learning by choosing a topic, setting a small goal, and practising consistently."
    elif any(word in text for word in ["python", "programming", "code"]):
        return "Python is a beginner-friendly programming language. Try practising variables, conditions, loops, and functions."
    elif any(word in text for word in ["internship", "codsoft"]):
        return "This chatbot is part of the CodSoft Artificial Intelligence internship task."
    elif any(word in text for word in ["thank", "thanks"]):
        return "You're welcome! 😊"
    elif any(word in text for word in ["bye", "goodbye", "see you"]):
        return "Goodbye! Have a great day. 👋"
    elif "help" in text:
        return "You can ask me about my name, Python, learning, courses, or this internship."
    elif text in ["", " "]:
        return "Please type a message so I can respond."
    else:
        return "I don't know how to answer that yet. Try asking about Python, courses, learning, or the internship."

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! I'm CodBot. Ask me something to get started."}
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

prompt = st.chat_input("Type your message...")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    response = get_response(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.rerun()

with st.sidebar:
    st.subheader("About this project")
    st.write("The chatbot checks user input for predefined keywords and selects a matching response using conditional statements.")
    if st.button("Clear conversation"):
        st.session_state.messages = [
            {"role": "assistant", "content": "Hi! I'm CodBot. Ask me something to get started."}
        ]
        st.rerun()

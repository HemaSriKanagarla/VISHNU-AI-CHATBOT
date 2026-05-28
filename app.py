import streamlit as st
from rag_pipeline import chain

st.set_page_config(
    page_title="Vishnu AI Chatbot",
    page_icon="🤖"
)

st.title("🤖 Vishnu AI Chatbot")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
prompt = st.chat_input("Ask a question")

if prompt:

    # Show user message
    st.chat_message("user").markdown(prompt)

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    # Generate response
    with st.spinner("Thinking..."):

        response = chain.invoke(prompt)

    # Show assistant response
    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })
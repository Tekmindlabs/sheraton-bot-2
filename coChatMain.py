import streamlit as st
from typing import Literal
from dataclasses import dataclass
import cohere

co = cohere.Client(st.secrets["COHERE_API_KEY"])

# Streamlit header
st.set_page_config(page_title="Product Info Bot")
st.title("Product Info Bot (Using cohere chat endpoint)")
st.write("This chatbot provides information about products from MyVitaminStore.pk")

# Loading styles.css
def load_css():
    with open("static/styles.css", "r") as f:
        css = f"<style>{f.read()} </style>"
        st.markdown(css, unsafe_allow_html=True)

# Website-specific documents for MyVitaminStore.pk
website_docs = [
    {
        "title": "Vitamin D Supplement",
        "snippet": "Our Vitamin D supplement ensures you get your daily dose of sunshine, supporting bone health and immune function.",
    },
    {
        "title": "Omega-3 Fish Oil",
        "snippet": "Rich in EPA and DHA, our Omega-3 Fish Oil supports cardiovascular health and cognitive function.",
    },
    # Add more product descriptions here...
]

# ... rest of the code remains unchanged ...

def initialize_session_state():
    # ... (existing code for session state initialization)

def on_click_callback():
    # ... (existing code for on_click_callback)

def main():
    initialize_session_state()
    chat_placeholder = st.container()
    prompt_placeholder = st.form("chat-form")

    with chat_placeholder:
        for chat in st.session_state.chat_history[2:]:
            if chat["role"] == "User":
                msg = chat["message"]
            else:
                msg = chat["message"]

            div = f"""
            <div class = "chatRow 
            {'' if chat["role"] == 'Chatbot' else 'rowReverse'}">
                <img class="chatIcon" src = "app/static/{'elsa.png' if chat["role"] == 'Chatbot' else 'admin.png'}" width=32 height=32>
                <div class = "chatBubble {'adminBubble' if chat["role"] == 'Chatbot' else 'humanBubble'}">&#8203; {msg}</div>
            </div>"""
            st.markdown(div, unsafe_allow_html=True)

    with st.form(key="chat_form"):
        cols = st.columns((6, 1))

        # Display the initial message if it hasn't been sent yet
        if not st.session_state.initial_message_sent:
            cols[0].text_input(
                "Chat",
                placeholder="Hello, how can I assist you?",
                label_visibility="collapsed",
                key="customer_prompt",
            )
        else:
            cols[0].text_input(
                "Chat",
                value=st.session_state.input_value,
                label_visibility="collapsed",
                key="customer_prompt",
            )

        cols[1].form_submit_button(
            "Ask",
            type="secondary",
            on_click=on_click_callback,
        )

    st.session_state.input_value = cols[0].text_input

if __name__ == "__main__":
    main()

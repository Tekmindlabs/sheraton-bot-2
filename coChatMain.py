import streamlit as st
from typing import Literal
from dataclasses import dataclass
import cohere

co = cohere.Client(st.secrets["COHERE_API_KEY"])

# Streamlit header
st.set_page_config(page_title="Co:Chat - An LLM-powered chat bot")
st.title("Sheraton-Bot-2 (Using cohere chat endpoint) ")
st.write("This is a chatbot for a specific Hotel (Knowledge base is limited to Sheraton Hotel and can be customized)")

# Loading styles.css
def load_css():
    with open("static/styles.css", "r") as f:
        css = f"<style>{f.read()} </style>"
        st.markdown(css, unsafe_allow_html=True)

# Website-specific documents
website_docs = [
    {
        "title": "About Us",
        "snippet": "Our hotel is located in the heart of the city, providing easy access to nearby attractions and business districts. With luxurious rooms and exceptional amenities, we strive to create a comfortable and memorable stay for our guests.",
    },
    {
        "title": "Room Types",
        "snippet": "We offer a range of room types to cater to different needs. From luxurious suites to spacious twin rooms, each accommodation is designed with comfort and convenience in mind. Our rooms feature amenities such as high-speed internet, air-conditioning, and LED TVs.",
    },
    {
        "title": "Dining",
        "snippet": "Our hotel boasts a variety of dining options to satisfy every craving. From our signature restaurant serving international cuisine to a cozy cafe offering light bites, guests can enjoy a diverse range of culinary experiences without leaving the premises.",
    },
]

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

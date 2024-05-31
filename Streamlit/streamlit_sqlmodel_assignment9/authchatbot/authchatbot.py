import os
import streamlit as st
from sqlmodel import Session, SQLModel, create_engine, select
from streamlit_option_menu import option_menu
from streamlit_cookies_manager import EncryptedCookieManager
from models import User, Message


st.title("Wellcome to my ChatBot")

# Part1 : connect to the database
@st.cache_resource
def connect_to_database():
    engine = create_engine("sqlite:///authchatbotdatabase.db")
    SQLModel.metadata.create_all(engine)
    return engine

engine = connect_to_database()  

# Part2: auth

with st.sidebar:
    selected = option_menu("Chat Bot", ["signing in", 'signing up'], 
        icons=['house', 'house'], menu_icon="cast", default_index=1)
    

if selected == "signing in":

    with st.form("Sign in"):
        st.header("Sign in")

        username = st.text_input("Username")
        password = st.text_input("Password")

        # Every form must have a submit button.
        signedin = st.form_submit_button("Signin")
        signedup = False
        

elif selected == "signing up":

    with st.form("Sign up"):
        st.header("Sign up")

        name = st.text_input("Name")
        email = st.text_input("Email")
        age = st.text_input("Age")
        username = st.text_input("Username")
        password = st.text_input("Password")

        # Every form must have a submit button.
        signedup = st.form_submit_button("Signup")
        signedin = False

     


# Enter chatbot after user signed in or signed up
if signedup or signedin:


    def ai(user_text_message):
        ai_text_message = user_text_messeag * 3
        return ai_text_message

    def process(user_text_message):
        ai_text_message = ai(user_text_message)

        # backend
        user_message = Message(text=user_text_message,
                               type="user",
                                 user_id=1)
       
        ai_message = Message(text=ai_text_message,
                              type="ai",
                                user_id=1)

        
        with Session(engine) as session:
            session.add(user_message)
            session.add(ai_message)
            session.commit()

        # frontend
        st.session_state.messages.append({"type":"user", "text":user_text_messeag})
        st.session_state.messages.append({"type":"ai", "text":ai_text_message})
        return ai_text_message

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["type"]):
            st.write(message["text"])


    if user_text_messeag := st.chat_input("Send a new message ..."):

        ai_text_message = process(user_text_messeag)

        with st.chat_message("user"):
            st.write(user_text_messeag)

        with st.chat_message("ai"):
            st.write(ai_text_message)



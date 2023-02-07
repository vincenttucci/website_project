from dotenv import load_dotenv
import openai
import os
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage", page_icon = "lol", layout = "wide")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


#LOAD ASSETS
def loadnem(url):
    req = requests.get(url)
    if req.status_code != 200:
        return None
    return req.json()

load_dotenv()
openai.api_key = os.getenv("api_key")

#WEBSITE DESIGNER
#ASSETS
computeranalystguy = loadnem("https://assets7.lottiefiles.com/packages/lf20_i2eyukor.json")
#HEADER
st.subheader("Introducing <Insert Name Here>")
st.title("Alpha Version 0.1.03")

#Function to take user input
def cool_ai_stuff(ticker):
    cheesenem = ("Write a 1500 word financial and corporate summary of " + str(ticker))
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt = cheesenem,
        temperature=0.3,
        max_tokens=3827,
        top_p=0.61,
        frequency_penalty=0,
        presence_penalty=0
    )
    return str(response.choices[0].text)


with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        user_input = st.text_input("Enter Company Here")
        if st.button("Click to run"):
            st.download_button("Download data as .txt", str(cool_ai_stuff(user_input)))

        st.text("Description: Enter a company in the search bar, click enter, then click")
        st.text("the button. Wait about a minute and a document should generate.")
        st.text("Once the document has generated, a download button will appear that you can click.")
        st.text("Some precaution messages may appear but just accept them, it just downloads a docx.")
    with right_column:
        st_lottie(computeranalystguy, height = 300, key = "coding", loop=False)





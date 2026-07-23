import streamlit as st
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from prompt import email_prompt
import os

load_dotenv()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama3-8b-8192"
)

st.title("📧 AI Email Generator")

topic = st.text_input("Enter Email Topic")

email_type = st.selectbox(
    "Select Email Type",
    [
        "Formal",
        "Informal",
        "Leave Application",
        "Complaint",
        "Appreciation"
    ]
)

if st.button("Generate Email"):

    if topic.strip() == "":
        st.warning("Please enter an email topic.")
    else:
        final_prompt = email_prompt.format(
            topic=topic,
            email_type=email_type
        )

        response = llm.invoke(final_prompt)

        st.subheader("Generated Email")
        st.write(response.content)
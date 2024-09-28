
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

## Prompt Template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a professionnal HR bot. Im gonna give you a job description and you are going to extract the following informations keys in the json format : Company name, Job general informations, Job title, Job mission, Responsabilities, Technical skills required "),
        ("user","jobDescriptionContent:{jobDescriptionContent}")
    ]
)
## streamlit framework

st.title('Langchain Demo With LLAMA3 API')
input_text=st.text_input("parse your job description")

# ollama LLAma2 LLm 
llm=Ollama(model="llama3")
output_parser=JsonOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"jobDescriptionContent":input_text}))
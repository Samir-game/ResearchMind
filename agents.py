from langchain.agents import create_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from tools import web_search , scrape_url 
from dotenv import load_dotenv
import os 

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    temperature=0
)

#1st agent-this agent will give real time data
def build_search_agent():
    return create_agent(
        model = llm,
        tools= [web_search]
    )


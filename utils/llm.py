import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import GROQ_API_KEY, LLM_MODEL_NAME 
from langchain_groq import ChatGroq

def initialize_llm() -> ChatGroq:
    """
    Initializes and returns the ChatGroq LLM.
    """

    llm = ChatGroq(
        temperature=0,
        groq_api_key=GROQ_API_KEY,
        model_name=LLM_MODEL_NAME
    )
    return llm
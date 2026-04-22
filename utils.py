import os
from dotenv import load_dotenv
from crewai import LLM

def get_gemini_llm():
    """
    Initializes and returns the CrewAI LLM mapping to Google's Gemini API natively.
    Will default to 'gemini/gemini-1.5-pro' for capable reasoning.
    """
    # Load environment variables explicitly here so Streamlit catches hot-reloads of .env
    load_dotenv(override=True)
    
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable is not set. Please check your .env file.")

    # CrewAI v1+ natively wraps Litellm, we use the LLM component natively:
    llm = LLM(
        model="gemini/gemini-flash-latest",
        api_key=api_key,
        temperature=0.5
    )
    return llm

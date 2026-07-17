import os

from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI

load_dotenv()

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

llm = ChatMistralAI(
    model="mistral-large-latest",
    temperature=0.2,
    api_key=MISTRAL_API_KEY,
)
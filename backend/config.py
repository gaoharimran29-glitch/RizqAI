import os
from langchain_mistralai import ChatMistralAI

load_dotenv()

llm = ChatMistralAI(
    model="mistral-large-latest",
    temperature=0.2,
    api_key=MISTRAL_API_KEY,
)
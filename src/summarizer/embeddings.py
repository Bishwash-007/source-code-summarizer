import getpass, os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from config import GEMINI_EMBED_MODEL

def get_embeddings():
    if not os.environ.get("GOOGLE_API_KEY"):
        os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google Gemini API key: ")
    print("Using Gemini embeddings model:", GEMINI_EMBED_MODEL)
    return GoogleGenerativeAIEmbeddings(model=GEMINI_EMBED_MODEL)
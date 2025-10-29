from langchain_google_genai import ChatGoogleGenerativeAI
from config import GEMINI_LLM_MODEL

def get_llm():
    print("Initializing Gemini model:", GEMINI_LLM_MODEL)
    return ChatGoogleGenerativeAI(model=GEMINI_LLM_MODEL)

def summarize_chunk(llm, chunk):
    
    prompt = f"""
        You are an expert JavaScript reviewer.

        File: {chunk.metadata.get('source') or 'unknown'}
        ---
        ```js
        {chunk.page_content}
        ```
        Summarize:
            1.	Purpose of this code.
            2.	Main functions/classes.
            3.	Any issues or improvements. """

    return llm.invoke(prompt).content
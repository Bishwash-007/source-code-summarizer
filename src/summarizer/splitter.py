from langchain_text_splitters import RecursiveCharacterTextSplitter, Language
from config import CHUNK_SIZE, CHUNK_OVERLAP

def split_code(docs):
    splitter = RecursiveCharacterTextSplitter.from_language(
        language=Language.JS,
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )
    chunks = splitter.split_documents(docs)
    print(f"Split into {len(chunks)} code chunks")
    return chunks
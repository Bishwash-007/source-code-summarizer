from langchain_chroma import Chroma
from config import DB_DIR

def build_vector_store(docs, embeddings):
    print("Building Chroma vector store...")
    vector_store = Chroma.from_documents(
        documents=docs,
        collection_name="js_source_code",
        embedding=embeddings,
        persist_directory=DB_DIR,
    )
    print("Vector store created at:", DB_DIR)
    return vector_store

def load_vector_store():
    print("Loading existing vector store...")
    return Chroma(
        collection_name="js_source_code",
        persist_directory=DB_DIR,
    )
from langchain_community.document_loaders.generic import GenericLoader
from langchain_community.document_loaders.parsers import LanguageParser
from langchain_text_splitters import Language
from config import REPO_PATH, LANGUAGE

def load_source_code():
    loader = GenericLoader.from_filesystem(
        REPO_PATH,
        glob="**/*",
        suffixes=['.js','html''css','jsx'],
        parser=LanguageParser(language=LANGUAGE, parser_threshold=1000),
    )
    docs = loader.load()
    print(f"Loaded {len(docs)} Code Chunks")
    return docs
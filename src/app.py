from flask import Flask, jsonify, request
from summarizer.repo_manager import clone_or_update_repo
from summarizer.loader import load_source_code
from summarizer.splitter import split_code
from summarizer.embeddings import get_embeddings
from summarizer.vectorstore import build_vector_store, load_vector_store
from summarizer.llm_model import get_llm, summarize_chunk

app = Flask(__name__)

@app.route("/build", methods=["POST"])
def build_index():
    
    try:
        clone_or_update_repo()
        docs = load_source_code()
        chunks = split_code(docs)
        embeddings = get_embeddings()
        build_vector_store(chunks, embeddings)
        return jsonify({"message": f"Indexed {len(chunks)} chunks."})

    except Exception as e:
        print(f"something went wrong: {e}")
        return jsonify({"error": str(e)}), 500

@app.route("/summarize", methods=["GET"])
def summarize_repo():
    try:
        clone_or_update_repo()
        docs = load_source_code()
        chunks = split_code(docs)
        llm = get_llm()
        summaries = [summarize_chunk(llm, c) for c in chunks]
        return jsonify({"summary_count": len(summaries), "summaries": summaries})
    
    except Exception as e:
        print(f"something went wrong: {e}")
        return jsonify({"error": str(e)}), 500
        

@app.route("/query", methods=["POST"])
def query_code():
    try:
        data = request.get_json()
        query = data.get("query")
        vector_store = load_vector_store()
        results = vector_store.similarity_search(query, k=4)
        response = [
            {
                "file": r.metadata.get("source"),
                "snippet": r.page_content[:300] + "..."
            }
            for r in results
        ]
        return jsonify({"query": query, "results": response})
        
    except Exception as e:
        print(f"Error in /query route: {e}")
        return jsonify({"error": str(e)}), 500
        

if __name__ == "__main__":
    app.run(debug=True, port=5000)
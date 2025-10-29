Source Code Analysis (RAG)
---
This simple flask app lets you summarize your code base.

Tech Stack
---
- Langchain
- ChromaDB
- GoogleGenAI
- Flask

To Run Locally
------

```bash
git clone https://github.com/bishwash-007/source-code-summarizer

cd source-code-summarizer

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python3 src/app.py
```

Setup Environment Variables
------
you can use other inference providers like openAI or Hugging face refer to their docs for the modification

```.env
GOOGLE_API_KEY=
```

Test Your Endpoints
---
```bash
# Build index
curl -X POST http://127.0.0.1:5000/build

# Summarize
curl http://127.0.0.1:5000/summarize

# Query
curl -X POST http://127.0.0.1:5000/query \
  -H "Content-Type: application/json" \
  -d '{"query":"What does this mean ...{your_question}"}'

```
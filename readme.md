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

```zsh
git clone https://github.com/bishwash-007/source-code-summarizer

cd source-code-summarizer

python3 -m venv venv
source venv/bin/activate

python3 src/app.py
```

Setup Environment Variables
------
you can use other inference providers like openAI or Hugging face refer to their docs for the modification

```.env
GOOGLE_API_KEY=
```
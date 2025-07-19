from flask import Flask, request, jsonify
from llama_index.llms.ollama import Ollama
from llama_index.core import Settings, VectorStoreIndex, SimpleDirectoryReader
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

import logging
# Set up logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
logging.info("Starting Flask application...")

# Load the index
# Configure Ollama to use Phi-3
Settings.llm = Ollama(model="phi3", base_url="http://localhost:11434")
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")

# Load documents and create the index
logging.info("Loading documents and creating index...")
documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents)
# Save the index to a file
query_engine = index.as_query_engine()
logging.info("Index loaded successfully.")


@app.route("/query", methods=["POST"])
def query():
    data = request.json
    prompt = data.get("prompt", "")

    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    response = query_engine.query(prompt)
    return jsonify({"response": str(response)})
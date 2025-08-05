from flask import Flask, request, jsonify
from llama_index.core import Settings, VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

app = Flask(__name__)
import os
os.environ["PYTORCH_ENABLE_MPS_FALLBACK"] = "1"
os.environ["PYTORCH_MPS_HIGH_WATERMARK_RATIO"] = "0"
os.environ["PYTORCH_MPS_FALLBACK"] = "1"
os.environ["TOKENIZERS_PARALLELISM"] = "false"

# Micro LLM + Micro Embed Model
Settings.llm = Ollama(model="phi", base_url="http://localhost:11434")
# Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
Settings.embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2", device="cpu")
# Load data
documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()

@app.route("/query", methods=["POST"])
def query():
    prompt = request.json.get("prompt", "")
    if not prompt:
        return jsonify({"error": "Missing prompt"}), 400
    response = query_engine.query(prompt)
    return jsonify({"response": str(response)})

#!/bin/bash

echo "Starting entrypoint script..."

# Start Ollama in the background only if not running
if ! curl -s http://localhost:11434/version > /dev/null; then
  ollama serve &
  echo "Ollama server starting..."
else
  echo "Ollama server already running."
fi

# Wait for Ollama to respond
until curl -s http://localhost:11434/version > /dev/null; do
  sleep 2
  echo "Waiting for Ollama to start..."
done
echo "Ollama server started."

# Pull the model
ollama pull phi3

# Wait for the model to be available
until ollama show phi3 > /dev/null 2>&1; do
  sleep 3
  echo "Waiting for phi3 model to be available..."
done

# Activate venv and install requirements
source /app/venv/bin/activate
pip install --break-system-packages -r /app/requirements.txt

# Start uWSGI
uwsgi
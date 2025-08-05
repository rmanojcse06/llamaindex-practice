#!/bin/sh
echo "Inside start.sh"
export TOKENIZERS_PARALLELISM=false
python3 -m venv ENV
source ./ENV/bin/activate
pip install --break-system-packages -r requirements.txt
ollama pull phi3
uwsgi --ini uwsgi.ini
echo "Exiting start.sh"
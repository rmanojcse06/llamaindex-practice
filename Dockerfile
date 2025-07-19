FROM ollama/ollama:latest

# Set working directory
WORKDIR /app

# System updates + install Python/uWSGI
RUN apt-get update && \
    apt-get install -y curl python3 python3-pip uwsgi uwsgi-plugin-python3

# Copy everything into the container
COPY /data /app/data
COPY app.py /app/
COPY uwsgi.ini /app/


# Install Python virtual environment module
RUN apt-get install -y python3-venv

# Create and activate a virtual environment
RUN python3 -m venv /app/venv
ENV PATH="/app/venv/bin:$PATH"
#RUN source /app/venv/bin/activate
# Upgrade pip and install dependencies within the venv
COPY requirements.txt /app/
RUN pip3 install --break-system-packages -r requirements.txt

# Expose API port
EXPOSE 5000
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh 
# Start Ollama service + uWSGI via entrypoint
ENTRYPOINT ["bash", "entrypoint.sh"]
#CMD ["bash", "-c", "ollama serve & sleep 2 && ollama pull phi3 && sleep 3 && uwsgi --ini uwsgi.ini"]

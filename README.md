# llamaindex-practice
To Learn Llama index to retrieve data from my daily uploads

Step (1): Install ollama using docker image

# Build the image with a custom name
```
docker build -t ollama-llamaindex-1 .
```




# Run the container with a name
```
docker run -d --name ollama-llamaindex-1-container -p 5000:5000 ollama-llamaindex-1
```




```
docker run -d -v ollama:/root/.ollama -p 15434:11434 --name ollama-llamaindex-practice ollama/ollama
```
Check if ollama running using curl command
```
curl -v http://localhost:11434
docker exec -it ollama-llamaindex-practice bash
ollama pull phi3:3.8b
```
docker exec -it ollama ollama pull phi3-3.8b:latest
``` 
echo %date% %time% && curl -v http://localhost:11434/api/generate -H "Content-Type: application/json" -d "{\"model\":\"phi4-mini\",\"prompt\":\"Who is Sachin Tendulkar?\",\"stream\":false}"
```


```
[wsl2]
memory=8GB
processors=4
swap=4GB
localhostForwarding=true
```
add this to %userprofile%\.wslconfig
and shutdown wsl --shutdown


```
python -m venv ENV
ENV\Scripts\activate

```








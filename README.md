# scopus_data_ajman_analysis
This is a simple project built with Streamlit to visualize the Scopus research data coming out of Ajman University  

Project is hosted on HuggingFace: https://huggingface.co/spaces/ahishamm/biassignment1

#### Installation 
- To install this locally, you need to create a conda environment 
```bash
conda create -n streamenv python=3.10 
conda activate streamenv 
pip install -r requirements.txt 
streamlit run app.py
```
#### Deployment as a Docker Container 
- To create a Docker container, a Dockerfile is provided. Make sure Docker Desktop is installed. The Dockerfile contains the following
```bash
FROM python:3.10-slim
ADD . .
RUN pip install -r requirements.txt 
EXPOSE 7250
ENTRYPOINT ["streamlit","run"] 
CMD ["./app.py","--server.headless","true","--server.fileWatcherType","none","--browser.gatherUsageStats","false","--server.port=7250","--server.address=0.0.0.0"]
```
- To build the Docker image from the Dockerfile, run the following command in the terminal or powershell: 
```bash
docker build -t scopusimage . 
```

- To run a Docker container with the name 'scopuscontainer' on port 7250 
```bash
docker run -p 7250:7250 --name scopuscontainer scopusimage
```

#### Project Preview (Updated)
Preview 1. 
<img width="1440" alt="Screenshot 2023-04-30 at 6 09 06 PM" src="https://user-images.githubusercontent.com/40188935/235357607-d12167c6-aa77-452a-ab90-53158486d5c1.png">
Preview 2. 
<img width="1440" alt="Screenshot 2023-04-30 at 6 09 13 PM" src="https://user-images.githubusercontent.com/40188935/235357621-973be212-a4b1-4d7c-a846-6182436079c5.png">
Preview 3. 
<img width="1440" alt="Screenshot 2023-04-30 at 6 11 25 PM" src="https://user-images.githubusercontent.com/40188935/235357637-19b5313b-fd95-43ee-8143-427d8934d48f.png">
Preview 4. 
<img width="1440" alt="Screenshot 2023-04-30 at 6 11 33 PM" src="https://user-images.githubusercontent.com/40188935/235357656-61bb8239-8efa-4a11-865b-dd4ac2caad0b.png">



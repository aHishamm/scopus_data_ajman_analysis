# scopus_data_ajman_analysis
This is a simple project built with Streamlit to visualize the Scopus research data coming out of Ajman University  

Project is hosted on HuggingFace: https://huggingface.co/spaces/ahishamm/biassignment1


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

#### Project Preview
Preview 1. 
<img width="1440" alt="Screenshot 2023-04-21 at 3 25 17 PM" src="https://user-images.githubusercontent.com/40188935/233624696-36da0345-0d74-4719-8413-53ac8cf7e89d.png">
Preview 2. 
<img width="1440" alt="Screenshot 2023-04-21 at 3 25 37 PM" src="https://user-images.githubusercontent.com/40188935/233624738-07a6504c-452b-4672-b7e9-4ff5ffaa73d1.png">
Preview 3. 
<img width="1440" alt="Screenshot 2023-04-21 at 3 25 54 PM" src="https://user-images.githubusercontent.com/40188935/233624794-f0e7c048-059e-43b2-ae1d-4e2de66968c7.png">


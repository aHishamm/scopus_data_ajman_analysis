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

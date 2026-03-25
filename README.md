# Genesetask — CI/CD Pipeline
 
A simple Flask web application with a complete end-to-end DevOps pipeline built from scratch.
 
---
 
## Live Demo
 
- **Live App:** https://genesetask.onrender.com
- **Docker Hub:** https://hub.docker.com/r/bishal64/genesetask/tags
 
---
 
## What This Project Does
 
This project demonstrates a full CI/CD pipeline that:
 
- Takes code from GitHub
- Automatically runs tests on every push
- Builds a Docker image
- Pushes the image to Docker Hub
- Deploys the live app automatically on Render
 
---

## How to Run Locally
 
### Option 1 — Run with Python
 

# 1. Clone the repo
git clone https://github.com/bishalrauniyar/genesetask.git
cd genesetask
 
# 2. Install dependencies
pip install -r requirements.txt
 
# 3. Run the app
python app.py

 
Visit `http://localhost:5000`


### Option 2 — Run with Docker
 

# 1. Pull image from Docker Hub
docker pull bishalrauniyar/genesetask:latest
 
# 2. Run the container
docker run -p 5000:5000 bishalrauniyar/genesetask:latest

 
Visit `http://localhost:5000`

## Docker
 
Step 1: Build image locally
 docker build -t genesetask .
 
Step 2: Run container locally
 docker run -p 5000:5000 genesetask


Step 3 View running containers
 docker ps

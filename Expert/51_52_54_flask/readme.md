

folder struture 
it should look like it

flask-docker/
│
├── app.py                # Your main Flask application
├── Dockerfile            # The Dockerfile to build the image
├── requirements.txt      # Python dependencies (Flask)
└── .dockerignore         # (Optional) List of files to exclude from Docker build
venv/
__pycache__/
*.pyc
.git/



1)

mkdir flask-docker
cd flask-docker

2)

python3 -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate


3) pip install Flask



only run these command under folder  flask docker


4) Docker commands

docker build -t flask-hello-world .


5) 

docker run -d -p 5000:5000 --name flask-container flask-hello-world

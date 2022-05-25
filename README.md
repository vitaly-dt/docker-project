# docker-project
Docker Project - A server in Flask

# How to use the flask app
In order to run the flask localy on you machine
make sure flask is installed: pip install --no-cache-dir -r requirements.txt
set the following env varible:
export FLASK_APP=server
export PORT 8080

Then run: flask run -h 0.0.0.0 -p $PORT

# Running the container
when running from the container, please read the comments in the DockerFile

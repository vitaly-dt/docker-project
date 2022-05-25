from flask import Flask
from flask import request

app = Flask(__name__)

json_msg = {
    "message": "I’m alive!",
}

json_err_msg = {
    "message": "Error! Wrong request!",
}

HTTP_METHODS = ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH']

@app.route("/directeam", methods=HTTP_METHODS)
def hello_directeam():
    if request.method != 'GET':
        return json_err_msg
    else:
        return json_msg
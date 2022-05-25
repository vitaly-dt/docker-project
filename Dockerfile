# Build a flask image, that server local server.py app
# listening on port 8080, from all inbound trafic
# To build: docker build -t flask-server:v1.4 .
# to run docker run -p 8080:8080 flask-server:v1.4
FROM python:3

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY server.py /app

ENV FLASK_APP=server
ENV PORT 8080

EXPOSE 8080

CMD [ "sh", "-c", "flask run -h 0.0.0.0 -p $PORT" ]
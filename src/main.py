from flask import Flask, jsonify, render_template
import socket
import sys
import logging

app = Flask(__name__)

root = logging.getLogger()
root.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
log_format = '%(name)s - %(levelname)s - %(message)s'
formatter = logging.Formatter(log_format)
handler.setFormatter(formatter)
root.addHandler(handler)
log =logging.getLogger("pythonLogger")

def fetchDetails():
    hostname = socket.gethostname()
    host_ip = socket.gethostbyname(hostname)
    return str(hostname), str(host_ip)

@app.route("/")
def hello_world():
    log.info("Root endpoint.")
    return "<p>Hello, World!</p>"

@app.route("/health")
def health():
    log.info("Checking health endpoint.")
    return jsonify(
        status="UP",
        code=200
    )

@app.route("/details")
def details():
    log.debug("Debug details endpoint.")
    hostname, ip = fetchDetails()
    return jsonify(
        HOSTNAME=hostname, 
        IP=ip
    )
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


#python3 -e venv virenv
#python3 -m venv venv 
#source venv/bin/activate
#
#
#   flask --app main run 

#Docker
#   docker login
#   docker build -t flaskpythonlogs:0.1 .
#   docker tag flaskpythonlogs sharma4rajesh/flaskpythonlogs:0.2
#   docker tag pythonlogsimg:0.2 sharma4rajesh/pythonlogsimg:0.2
#   docker push sharma4rajesh/flaskpythonlogs:0.2
#   docker run -d -p 80:5001 --name pythonlogs flaskpythonlogs:0.3
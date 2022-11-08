from flask import Flask
import os
import socket

app = Flask(__name__)
ok = socket.gethostname()
ip = socket.gethostbyname(ok)


@app.route("/")
def hello():
    return str(ip)


app.run(host="0.0.0.0")

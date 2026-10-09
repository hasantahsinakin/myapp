from flask import Flask
import os, socket

app = Flask(__name__)

@app.get("/")
def index():
    return f"Merhaba! Commit: 2 Pod: {socket.gethostname()} - Versiyon: {os.getenv('APP_VERSION', 'dev')}\n"

@app.get("/healthz")
def healthz():
    return "ok"

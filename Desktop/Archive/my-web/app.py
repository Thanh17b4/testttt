import uvicorn as uvicorn
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello, world!'


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("/")


@app.route("/dashboard")
def dashboard():
    return render_template("/football.html")


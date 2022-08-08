from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/blog")
def blog():
    return "This is a blog"


@app.route("/html")
def html():
    return render_template('index.html')

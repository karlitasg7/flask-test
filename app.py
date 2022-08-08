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


@app.route("/<username>")
def hello_world_name(username=None):
    return render_template('index.html', name=username)


@app.route("/<username>/<int:age>")
def hello_world_name_age(username=None, age=None):
    return render_template('index.html', name=username, age=age)

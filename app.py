from flask import Flask

app = Flask(__name__)

# Try to deploy to local OS cluster!

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p> Welcome to OS cluster!"

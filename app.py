from flask import Flask

app = Flask(__name__)

# Try to deploy to local OS cluster!

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p> Welcome to OS cluster!"

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8001)
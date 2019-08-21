from flask import Flask

PORT = 8000

app = Flask(__name__)

@app.route("/")
def root():
    result = "Hello, world!\n".encode("utf-8")
    return result

@app.route("/user/<username>")
def show_user(username):
    return ("Hello, %s\n" % username).encode("utf-8")

@app.route("/user/<username>/<message>")
def show_user_and_message(username, message):
    return ("Hello, %s\nHere's a message: %s\n" % (username, message)).encode("utf-8")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT)

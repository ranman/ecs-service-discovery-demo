from flask import Flask
import socket
app = Flask(__name__)

@app.route("/")
def do_work():
    return "I'm a worker and I'm doing some work!"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)

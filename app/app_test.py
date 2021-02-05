import sys, os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def helloBg():
    return "hello BG"

@app.route('/ma_route/<name>')
def displayVar(name):
    return name

if __name__ == "__main__":
    print("Hello")
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
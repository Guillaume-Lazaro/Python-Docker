import sys, os
from flask import Flask

app = Flask(__name__)

#route for home page
# @app.route("/")
# def index():
#     return "Hello AP Formation 🤖 ! \n\nCeci est une micro application python faite avec Flask 🐍 \n\n"

@app.route('/')
def helloBg():
    return 'hello BG'
    
if __name__ == "__main__":
    # print(index())
    app.run(debug=True, port=5000)


import sys, os, json
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def helloBg():
    return "hello my app"

@app.route('/ma_route/<name>')
def displayVar(name):
    return name

# instanciation
books = [
	{
		'id':1,
		'titre' : 'un titre',
	},
	{
		'id':2,
		'titre': 'un autre titre random',
	}
]
books_json = json.dumps(books)

@app.route("/api/books")
def displayBooks():
    return books_json

@app.route("/api/books/id/<id>")
def getBookFromId(id):
    index = int(id)
    return books[index]

@app.route("/api/books/title/<title>")
def getBookFromTitle(title):
    for item in books:
        if item['titre'] == title:
            return item

    return "Aucun livre de ce titre la"

if __name__ == "__main__":
    print("Hello")
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
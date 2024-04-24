from flask import *

app = Flask(__name__)

@app.route("/")
def deck():
    return render_template("deck.html")

@app.post("/insertItem")
def insertItem():
    item = request.json
    try:

        return f'added item {item}', 200
    except:
        return 400


@app.get("/readItem/<ID>")
def readItem(ID):
    print(ID)
    return '200'

app.put("/updateItem")
def updateItem():
    item = request.json

    try:
        return f'updated item {item}', 200
    except:
        return 400
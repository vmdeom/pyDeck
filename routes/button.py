from flask import Blueprint, request, jsonify
from models.Button import Button
from sqlmodel import session, select
from database import engine

button_bp = Blueprint("button", +__name__)

@app.route("/")
def deck():
    return render_template("deck.html")

@button_bp.route("/item", methods=["POST"])
def insert_item():
    item = request.json
    try:

        return f"added item {item}", 200
    except:
        return 400


@button_bp.route("/item/<ID>", methods=["GET"])
def read_item(ID):
    print(ID)
    return 200

@button_bp.route("/item", methods=["PATCH"])
def update_item():
    item = request.json

    try:
        return f"updated item {item}", 200
    except:
        return 400

@button_bp.route("/item", methods=["DELETE"])
def delete_item():
    pass
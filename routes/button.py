from flask import Blueprint, request, jsonify
from sqlmodel import Session, select
from models.Button import Button
from database import engine

button_bp = Blueprint("button", __name__)

@button_bp.route("/button", methods=["POST"])
def post_button():
    button_data = request.json
    button = Button(**button_data)
    try:
        with Session(engine) as session:
            session.add(button)
            session.commit()
            session.refresh(button)
        
        return jsonify(button.dict()), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@button_bp.route("/button/<code>", methods=["GET"])
def get_button(code: str):
    with Session(engine) as session:
        query = select(Button).where(Button.code == code)
        button = session.exec(query).first()
        if button:
            return jsonify(button.dict()), 200

    return jsonify({"error": "not found"}), 404

@button_bp.route("/get_buttons", methods=["GET"])
def get_buttons():
    with Session(engine) as session:
        buttons = session.exec(select(Button)).all()
        if buttons:
            return [{     
                "effect_type": button.effect_type,
                "effect_dir": button.effect_dir,
                "name": button.name,
                "color": button.color,
                "icon": button.icon,
                "page": button.page,
                "code": button.code} for button in buttons], 200
        return jsonify({"error": "not found"}), 404

@button_bp.route("/button/<code>", methods=["PATCH"])
def patch_button(code: str):

    button_data = request.json

    with Session(engine) as session:
        query = select(Button).where(Button.code == code)
        button = session.exec(query).first()
        
        if not button:
            return jsonify({"error": "not found"}), 404

        for key, value in button_data.items():
            if hasattr(button, key):
                setattr(button, key, value)
        
        session.add(button)
        session.commit()
        session.refresh(button)

        return jsonify(button.dict()), 200
    
    return jsonify({"error": "not found"}), 404

@button_bp.route("/button/<code>", methods=["DELETE"])
def delete_button(code: str):
    try:
        with Session(engine) as session:
            query = select(Button).where(Button.code == code)
            button = session.exec(query).first()

            if not button:
                return jsonify({"error": "not found"}), 404
            
            session.delete(button)
            session.commit()

        return jsonify(button.dict(), 200)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400
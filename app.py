from flask import Flask, render_template
from database import create_db_and_tables
from routes.button import button_bp

app = Flask(__name__, template_folder="src/templates")

create_db_and_tables()

app.register_blueprint(button_bp)

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/deck")
def deck():
    return render_template('deck/deck.html')

if __name__ == "__main__":
    app.run(debug=True)
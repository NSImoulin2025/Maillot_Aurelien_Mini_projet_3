from flask import Flask, render_template, jsonify, request
from Code_site import Jeu_du_simon

app = Flask(__name__)
Jeu = Jeu_du_simon()

@app.route('/')
def index():
    return render_template('html.html')

@app.route('/new_sequence', methods=['POST'])
def new_sequence():
    Jeu.debut()
    return jsonify(sequence=Jeu.get_sequence())

@app.route('/check_input', methods=['POST'])
def check_input():
    data = request.get_json()
    if not data or "sequence" not in data:
        return jsonify(success=False, error="Invalid input"), 400

    user_sequence = data.get("sequence", [])
    try:
        result = Jeu.vérifier_sequence(user_sequence)
        return jsonify(success=result, full_sequence=Jeu.get_sequence())
    except Exception as e:
        return jsonify(success=False, error=str(e)), 500

@app.route('/get_score', methods=['GET'])
def get_score():
    return jsonify(score=Jeu.get_score())

if __name__ == '__main__':
    app.run(port=8888)

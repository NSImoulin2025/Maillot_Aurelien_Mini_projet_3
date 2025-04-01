from flask import Flask, render_template, jsonify, request
from Code_site import Jeu_du_simon

app = Flask(__name__)
Jeu = Jeu_du_simon()

@app.route('/')
def index():
    """
    Route principale qui rend la page HTML du jeu.
    """
    return render_template('page.html')

@app.route('/new_sequence', methods=['POST'])
def new_sequence():
    """
    Démarre une nouvelle partie en réinitialisant la séquence et le score.
    Renvoie la nouvelle séquence générée.
    """
    Jeu.debut()
    return jsonify(sequence=Jeu.get_sequence())

@app.route('/check_input', methods=['POST'])
def check_input():
    """
    Vérifie si la séquence fournie par l'utilisateur correspond à la séquence du jeu.
    Renvoie un succès ou une erreur en cas de séquence incorrecte.
    """
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
    """
    Renvoie le score actuel du joueur.
    """
    return jsonify(score=Jeu.get_score())

@app.route('/play_turn', methods=['POST'])
def play_turn():
    """
    Gère un tour de jeu en vérifiant la séquence utilisateur.
    Renvoie le résultat (succès ou échec), la séquence complète et le score.
    """
    data = request.get_json()
    if not data or "sequence" not in data:
        return jsonify(success=False, error="Invalid input"), 400

    user_sequence = data.get("sequence", [])
    try:
        result = Jeu.vérifier_sequence(user_sequence)
        if result:
            return jsonify(success=True, full_sequence=Jeu.get_sequence(), score=Jeu.get_score())
        else:
            return jsonify(success=False, error="Incorrect sequence", score=Jeu.get_score())
    except Exception as e:
        return jsonify(success=False, error=str(e)), 500

if __name__ == '__main__':
    """
    Démarre le serveur Flask sur le port 8888.
    """
    app.run(port=8888)

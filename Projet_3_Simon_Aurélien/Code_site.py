import random

class Jeu_du_simon:
    """
    Classe représentant le jeu du Simon.
    Gère la séquence, le score et la logique de vérification.
    """

    def __init__(self):
        """
        Initialise une nouvelle instance du jeu avec une séquence vide et un score de 0.
        """
        self.sequence = []
        self.score = 0

    def debut(self):
        """
        Réinitialise le jeu en vidant la séquence et en réinitialisant le score.
        Ajoute une première couleur à la séquence.
        """
        self.sequence = []
        self.score = 0
        self.ajouter_couleur()

    def ajouter_couleur(self):
        """
        Ajoute une nouvelle couleur aléatoire (représentée par un entier entre 0 et 3) à la séquence.
        """
        self.sequence.append(random.randint(0, 3))

    def vérifier_sequence(self, sequence_joueur):
        """
        Vérifie si la séquence fournie par le joueur correspond à la séquence actuelle du jeu.

        Args:
            sequence_joueur (list): La séquence entrée par le joueur.

        Returns:
            bool: True si la séquence est correcte, False sinon.
        """
        for i in range(len(sequence_joueur)):
            if sequence_joueur[i] != self.sequence[i]:
                return False
        if len(sequence_joueur) == len(self.sequence):
            self.score += 1
            self.ajouter_couleur()
        return True

    def get_sequence(self):
        """
        Retourne la séquence actuelle du jeu.

        Returns:
            list: La séquence actuelle.
        """
        return self.sequence

    def get_score(self):
        """
        Retourne le score actuel du joueur.

        Returns:
            int: Le score actuel.
        """
        return self.score

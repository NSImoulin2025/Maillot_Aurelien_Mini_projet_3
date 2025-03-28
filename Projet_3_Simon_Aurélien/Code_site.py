import random

class Jeu_du_simon:
    def __init__(self):
        self.sequence = []
        self.score = 0  # Ajout du score

    def debut(self):
        self.sequence = []
        self.score = 0  # Réinitialiser le score
        self.ajouter_couleur()

    def ajouter_couleur(self):
        self.sequence.append(random.randint(0, 3))

    def vérifier_sequence(self, sequence_joueur):
        for i in range(len(sequence_joueur)):
            if sequence_joueur[i] != self.sequence[i]:
                return False
        if len(sequence_joueur) == len(self.sequence):
            self.score += 1  # Augmenter le score si la séquence est correcte
            self.ajouter_couleur()

        return True

    def get_sequence(self):
        return self.sequence

    def get_score(self):
        return self.score
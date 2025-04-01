document.addEventListener("DOMContentLoaded", () => {
    /**
     * Initialise les éléments du DOM et les événements pour le jeu.
     */
    const startButton = document.getElementById("start-btn");
    const buttons = document.querySelectorAll(".color-btn");
    const scoreDisplay = document.getElementById("score");
    let playerSequence = [];
    let gameSequence = [];
    let score = 0;

    startButton.addEventListener("click", async () => {
        /**
         * Démarre une nouvelle partie en envoyant une requête au serveur.
         * Réinitialise le score et joue la séquence initiale.
         */
        const response = await fetch("/new_sequence", { method: "POST" });
        const data = await response.json();
        gameSequence = data.sequence;
        score = 0;
        updateScore();
        playSequence();
    });

    buttons.forEach(button => {
        button.addEventListener("click", async (event) => {
            /**
             * Gère les clics sur les boutons de couleur.
             * Vérifie la séquence utilisateur et envoie les données au serveur.
             */
            const clickedButton = event.target;
            clickedButton.classList.add("active");
            setTimeout(() => clickedButton.classList.remove("active"), 300);

            playerSequence.push(parseInt(clickedButton.id));
            if (playerSequence.length === gameSequence.length) {
                const response = await fetch("/play_turn", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ sequence: playerSequence })
                });
                const data = await response.json();
                if (data.success) {
                    score = data.score;
                    updateScore();
                    gameSequence = data.full_sequence;
                    playerSequence = [];
                    setTimeout(playSequence, 1000);
                } else {
                    alert("Perdu ! Votre score final est : " + data.score);
                    playerSequence = [];
                }
            }
        });
    });

    function playSequence() {
        /**
         * Joue la séquence actuelle en activant les boutons correspondants.
         */
        let i = 0;
        const interval = setInterval(() => {
            const button = document.getElementById(gameSequence[i].toString());
            button.classList.add("active");
            setTimeout(() => button.classList.remove("active"), 500);
            i++;
            if (i >= gameSequence.length) clearInterval(interval);
        }, 1000);
    }

    function updateScore() {
        /**
         * Met à jour l'affichage du score dans le DOM.
         */
        scoreDisplay.textContent = `Score : ${score}`;
    }
});
document.addEventListener("DOMContentLoaded", () => {
    const startButton = document.getElementById("start-btn");
    const buttons = document.querySelectorAll(".color-btn");
    const scoreDisplay = document.getElementById("score");
    let playerSequence = [];
    let gameSequence = [];
    let score = 0;

    startButton.addEventListener("click", async () => {
        const response = await fetch("/new_sequence", { method: "POST" });
        const data = await response.json();
        gameSequence = data.sequence;
        score = 0; // Réinitialiser le score au début
        updateScore();
        playSequence();
    });

    buttons.forEach(button => {
        button.addEventListener("click", async (event) => {
            const clickedButton = event.target;
            clickedButton.classList.add("active");
            setTimeout(() => clickedButton.classList.remove("active"), 300);

            playerSequence.push(parseInt(clickedButton.id));
            if (playerSequence.length === gameSequence.length) {
                const response = await fetch("/check_input", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ sequence: playerSequence })
                });
                const data = await response.json();
                if (data.success) {
                    score++; // Augmenter le score si la séquence est correcte
                    updateScore();
                    gameSequence = data.full_sequence;
                    playerSequence = [];
                    setTimeout(playSequence, 1000);
                } else {
                    alert("Perdu ! Votre score final est : " + score);
                    playerSequence = [];
                }
            }
        });
    });

    function playSequence() {
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
        scoreDisplay.textContent = `Score : ${score}`;
    }
});
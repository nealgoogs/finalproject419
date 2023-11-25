function updatePasswordStrength() {
    const password = document.getElementById('password').value;
    const result = zxcvbn(password);
    const score = result.score;
    const runner = document.getElementById('runner-icon');
    const strengthMeterWidth = document.getElementById('password-strength-meter').offsetWidth;

    // Update runner position based on strength
    const runnerPosition = (result.score / 4) * strengthMeterWidth;
    runner.style.left = runnerPosition + 'px';

    if (score === 4) {
        triggerConfetti();
    }

}

function triggerConfetti() {
    confetti({
        particleCount: 100,
        spread: 70,
        origin: { y: 0.6 }
    });
}
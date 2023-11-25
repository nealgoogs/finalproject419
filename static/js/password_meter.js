function updatePasswordStrength() {
    const password = document.getElementById('password').value;
    const strengthMeter = document.getElementById('password-strength-meter');
    const strengthFeedback = document.getElementById('password-strength-feedback');

    if (password) {
        const result = zxcvbn(password);
        const score = result.score;

        // Update the strength meter color based on the score
        strengthMeter.style.backgroundColor = getColor(score);

        // Optional: Update feedback text based on password strength
        const feedbackText = ["Weak", "Fair", "Good", "Strong", "Very Strong"];
        strengthFeedback.textContent = "Strength: " + feedbackText[score];
    } else {
        // If the password field is empty, set the meter to white (or any other default color)
        strengthMeter.style.backgroundColor = 'white';
        strengthFeedback.textContent = '';
    }
}

// Initialize the strength meter color on page load
document.addEventListener('DOMContentLoaded', function() {
    updatePasswordStrength();
});


function getColor(score) {
    switch(score) {
        case 0: return '#ff3e36'; // Red
        case 1: return '#ff691f'; // Orange
        case 2: return '#f3d331'; // Yellow
        case 3: return '#0fbd4f'; // Light Green
        case 4: return '#00a300'; // Green
    }
}

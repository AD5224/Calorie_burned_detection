// script.js
document.getElementById('calorieForm').addEventListener('submit', function(event) {
    const duration = document.getElementById('duration').value;
    const weight = document.getElementById('weight').value;

    if (duration <= 0 || weight <= 0) {
        event.preventDefault();
        alert('Please enter positive values for duration and weight.');
    }
});

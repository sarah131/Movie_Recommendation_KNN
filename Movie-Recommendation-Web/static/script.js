function getRecommendations() {
    const userIndex = document.getElementById('userIndex').value;
    const recommendationsList = document.getElementById('recommendationsList');
    const errorMessage = document.getElementById('errorMessage');

    recommendationsList.innerHTML = '';
    errorMessage.textContent = '';

    if (userIndex === '') {
        errorMessage.textContent = 'Please enter a valid user index.';
        return;
    }

    fetch('/recommend', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ user_index: userIndex })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            errorMessage.textContent = data.error;
        } else {
            data.recommendations.forEach(movie => {
                const li = document.createElement('li');
                li.textContent = movie;
                recommendationsList.appendChild(li);
            });
        }
    })
    .catch(error => {
        errorMessage.textContent = 'An error occurred. Please try again.';
    });
}

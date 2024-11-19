let currentQuestion = 0;
const totalQuestions = questions.length;

function showQuestion(index) {
    const questionContainer = document.getElementById('question-container');
    const progressBar = document.getElementById('progress-bar');
    const question = questions[index];

    questionContainer.innerHTML = `
        <h3 class="mb-4">${question.question}</h3>
        <div class="options">
            <button onclick="submitAnswer('A')" class="btn btn-outline-primary mb-2 w-100">
                ${question.options.A}
            </button>
            <button onclick="submitAnswer('B')" class="btn btn-outline-primary w-100">
                ${question.options.B}
            </button>
        </div>
    `;

    progressBar.style.width = `${(index / totalQuestions) * 100}%`;
}

function submitAnswer(answer) {
    fetch('/submit_answer', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ answer: answer })
    })
    .then(response => response.json())
    .then(data => {
        currentQuestion++;
        if (currentQuestion < totalQuestions) {
            showQuestion(currentQuestion);
        } else {
            window.location.href = '/result';
        }
    });
}

document.addEventListener('DOMContentLoaded', () => {
    showQuestion(0);
});

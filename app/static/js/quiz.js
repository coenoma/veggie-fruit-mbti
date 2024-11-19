let currentQuestion = 0;
const totalQuestions = questions.length;

function showQuestion(index) {
    const questionContainer = document.getElementById('question-container');
    const progressBar = document.getElementById('progress-bar');
    const question = questions[index];

    questionContainer.innerHTML = `
        <h3 class="heading-2 mb-6">${question.question}</h3>
        <div class="space-y-4">
            <button onclick="submitAnswer('A')" class="w-full btn-outline">
                ${question.options.A}
            </button>
            <button onclick="submitAnswer('B')" class="w-full btn-outline">
                ${question.options.B}
            </button>
        </div>
    `;

    progressBar.style.width = `${(index / totalQuestions) * 100}%`;
}

function submitAnswer(answer) {
    const buttons = document.querySelectorAll('button');
    buttons.forEach(button => {
        button.disabled = true;
        button.classList.add('opacity-50');
    });

    fetch('/quiz/submit_answer', {
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
            setTimeout(() => {
                showQuestion(currentQuestion);
            }, 300);
        } else {
            window.location.href = '/result';
        }
    });
}

document.addEventListener('DOMContentLoaded', () => {
    showQuestion(0);
});

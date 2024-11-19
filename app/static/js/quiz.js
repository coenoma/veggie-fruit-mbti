let currentQuestion = 0;
const totalQuestions = questions.length;

function showQuestion(index) {
    const questionContainer = document.getElementById('question-container');
    const progressBar = document.getElementById('progress-bar');
    const question = questions[index];

    // アニメーション用のクラスを追加
    questionContainer.classList.add('opacity-0', 'translate-y-4');
    
    questionContainer.innerHTML = `
        <div class="mb-8">
            <h3 class="heading-2 mb-4">${question.question}</h3>
            <p class="text-gray-600 text-sm">質問 ${index + 1} / ${totalQuestions}</p>
        </div>
        <div class="space-y-4 md:space-y-6">
            <button onclick="submitAnswer('A')" 
                    class="w-full btn-outline transition-all duration-300 hover:scale-102 focus:outline-none focus:ring-2 focus:ring-primary-500">
                ${question.options.A}
            </button>
            <button onclick="submitAnswer('B')" 
                    class="w-full btn-outline transition-all duration-300 hover:scale-102 focus:outline-none focus:ring-2 focus:ring-primary-500">
                ${question.options.B}
            </button>
        </div>
    `;

    // フェードインアニメーション
    requestAnimationFrame(() => {
        questionContainer.classList.remove('opacity-0', 'translate-y-4');
        questionContainer.classList.add('transition-all', 'duration-500', 'ease-out');
    });

    // プログレスバーのアニメーション
    progressBar.style.transition = 'width 0.5s ease-out';
    progressBar.style.width = `${((index + 1) / totalQuestions) * 100}%`;
}

function submitAnswer(answer) {
    const buttons = document.querySelectorAll('button');
    buttons.forEach(button => {
        button.disabled = true;
        button.classList.add('opacity-50', 'cursor-not-allowed');
    });

    fetch('/quiz/submit_answer', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ answer: answer })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        currentQuestion++;
        if (currentQuestion < totalQuestions) {
            const questionContainer = document.getElementById('question-container');
            questionContainer.classList.add('opacity-0', 'translate-y-4');
            
            setTimeout(() => {
                showQuestion(currentQuestion);
            }, 300);
        } else {
            window.location.href = '/result';
        }
    })
    .catch(error => {
        console.error('Error:', error);
        showError('エラーが発生しました。もう一度お試しください。');
    });
}

function showError(message) {
    const errorDiv = document.createElement('div');
    errorDiv.className = 'fixed top-4 right-4 bg-red-100 border-l-4 border-red-500 text-red-700 p-4 rounded shadow-md';
    errorDiv.innerHTML = message;
    document.body.appendChild(errorDiv);
    
    setTimeout(() => {
        errorDiv.remove();
    }, 5000);
}

document.addEventListener('DOMContentLoaded', () => {
    showQuestion(0);
});

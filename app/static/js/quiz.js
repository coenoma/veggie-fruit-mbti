let currentQuestion = 0;
const totalQuestions = questions.length;

function showQuestion(index) {
    const questionContainer = document.getElementById('question-container');
    const progressBar = document.getElementById('progress-bar');
    const question = questions[index];
    
    // 進捗率を計算
    const progressPercentage = ((index + 1) / questions.length) * 100;
    
    // プログレスバーの更新（アニメーション付き）
    progressBar.style.transition = 'width 300ms ease-out';
    progressBar.style.width = `${progressPercentage}%`;
    progressBar.setAttribute('aria-valuenow', progressPercentage);
    progressBar.setAttribute('aria-valuemax', 100);
    
    // 質問表示を更新
    questionContainer.classList.add('opacity-0', 'translate-y-4');
    
    questionContainer.innerHTML = `
        <div class="question-wrapper">
            <h3 class="heading-2 mb-4">${question.question}</h3>
            <p class="text-gray-600 text-sm">質問 ${index + 1} / ${questions.length}</p>
        </div>
        <div class="options-container">
            <button onclick="submitAnswer('A')" 
                    class="answer-button w-full btn-outline transition-all duration-300 hover:scale-102 focus:outline-none focus:ring-2 focus:ring-primary-500">
                ${question.options.A}
            </button>
            <button onclick="submitAnswer('B')" 
                    class="answer-button w-full btn-outline transition-all duration-300 hover:scale-102 focus:outline-none focus:ring-2 focus:ring-primary-500">
                ${question.options.B}
            </button>
        </div>
    `;

    // フェードインアニメーション
    requestAnimationFrame(() => {
        questionContainer.classList.remove('opacity-0', 'translate-y-4');
        questionContainer.classList.add('transition-all', 'duration-500', 'ease-out');
    });
}

function submitAnswer(answer) {
    // 回答ボタンのみを無効化（診断中止ボタンには影響しない）
    const answerButtons = document.querySelectorAll('.answer-button');
    answerButtons.forEach(button => {
        button.disabled = true;
        button.classList.add('opacity-50', 'cursor-not-allowed');
    });

    fetch(submitUrl, {
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
        if (currentQuestion < questions.length) {
            const questionContainer = document.getElementById('question-container');
            questionContainer.classList.add('opacity-0', 'translate-y-4');
            
            setTimeout(() => {
                showQuestion(currentQuestion);
            }, 300);
        } else {
            window.location.href = resultUrl;
        }
    })
    .catch(error => {
        console.error('Error:', error);
        showError('エラーが発生しました。もう一度お試しください。');
        // エラー時は回答ボタンを再度有効化
        answerButtons.forEach(button => {
            button.disabled = false;
            button.classList.remove('opacity-50', 'cursor-not-allowed');
        });
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

// モーダル関連の処理をDOMContentLoadedイベントの中に移動
document.addEventListener('DOMContentLoaded', () => {
    const modal = document.getElementById('confirmModal');
    const stopButton = document.getElementById('stopButton');
    const continueButton = document.getElementById('continueButton');
    const modalContent = modal.querySelector('.bg-white');

    function showModal() {
        modal.classList.remove('hidden');
        modal.classList.add('flex');
        document.body.style.overflow = 'hidden';
    }

    function hideModal() {
        modal.classList.add('hidden');
        modal.classList.remove('flex');
        document.body.style.overflow = '';
    }

    // 診断中止ボタンのイベントリスナー
    stopButton.addEventListener('click', showModal);

    // 診断を続けるボタンのイベントリスナー
    continueButton.addEventListener('click', hideModal);

    // モーダルの外側をクリックした時にモーダルを閉じる
    modal.addEventListener('click', (event) => {
        if (!modalContent.contains(event.target)) {
            hideModal();
        }
    });

    // ESCキーでモーダルを閉じる
    document.addEventListener('keydown', (event) => {
        if (event.key === 'Escape') {
            hideModal();
        }
    });

    showQuestion(0);
});

// ESCキーでモーダルを閉じる
document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape') {
        hideModal();
    }
});

document.addEventListener('DOMContentLoaded', () => {
    showQuestion(0);
});

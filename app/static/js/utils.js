// Common utility functions
function showToast(message, type = 'info') {
    const toast = document.getElementById('toast-message');
    if (!toast) {
        const toastDiv = document.createElement('div');
        toastDiv.id = 'toast-message';
        toastDiv.className = `fixed bottom-4 right-4 p-4 rounded-lg shadow-lg transform transition-all duration-300 ${
            type === 'error' ? 'bg-red-500' : 'bg-primary-500'
        } text-white`;
        document.body.appendChild(toastDiv);
    }
    
    toast.textContent = message;
    toast.classList.remove('translate-y-full', 'opacity-0');
    
    setTimeout(() => {
        toast.classList.add('translate-y-full', 'opacity-0');
    }, 3000);
}

function disableButtons(buttons) {
    buttons.forEach(button => {
        button.disabled = true;
        button.classList.add('opacity-50', 'cursor-not-allowed');
    });
}

function enableButtons(buttons) {
    buttons.forEach(button => {
        button.disabled = false;
        button.classList.remove('opacity-50', 'cursor-not-allowed');
    });
}

export {
    showToast,
    disableButtons,
    enableButtons
};

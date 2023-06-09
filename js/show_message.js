// messageUtils.js
export function showMessage(message, color) {
    messageDiv.textContent = message;
    messageDiv.style.color = color;
    messageDiv.style.fontWeight = 'bold';
    messageDiv.style.marginTop = '10px';
}
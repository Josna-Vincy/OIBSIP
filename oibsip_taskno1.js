let displayValue = '';

function appendToDisplay(value) {
    displayValue += value;
    document.getElementById('display').value = displayValue;
}

function clearDisplay() {
    displayValue = '';
    document.getElementById('display').value = displayValue;
}

function calculateResult() {
    try {
        let result = eval(displayValue);
        document.getElementById('display').value = result;
        displayValue = '';
    } catch (error) {
        document.getElementById('display').value = 'Error';
        displayValue = '';
    }
}

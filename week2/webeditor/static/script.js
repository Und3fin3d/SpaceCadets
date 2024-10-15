const code = document.getElementById('code');
const button = document.getElementById('run');
const terminal = document.getElementById('terminal');
const terminalOutput = document.getElementById('terminal-output');
const closeTerminal = document.getElementById('close-terminal');
const lineNumbers = document.getElementById('line-numbers');
const socket = io();
const overlay = document.createElement('div');
overlay.style.position = 'absolute';
overlay.style.pointerEvents = 'none';
overlay.style.whiteSpace = 'pre-wrap';
overlay.style.wordWrap = 'break-word';
code.parentNode.insertBefore(overlay, code.nextSibling);

function updateOverlay() {
    overlay.style.top = code.offsetTop + 'px';
    overlay.style.left = code.offsetLeft + 'px';
    overlay.style.width = code.offsetWidth + 'px';
    overlay.style.height = code.offsetHeight + 'px';
    overlay.style.fontSize = window.getComputedStyle(code).fontSize;
    overlay.style.fontFamily = window.getComputedStyle(code).fontFamily;
    overlay.style.lineHeight = window.getComputedStyle(code).lineHeight;
    overlay.style.padding = window.getComputedStyle(code).padding;
}

function updateLineNumbers() {
    const lines = code.value.split('\n').length;
    lineNumbers.innerHTML = Array(lines).fill().map((_, i) => `<div>${i + 1}</div>`) .join('');
}

updateOverlay();
updateLineNumbers();
window.addEventListener('resize', updateOverlay);

button.addEventListener('click', () => {
    const txt = code.value;
    socket.emit('run', txt);
    terminal.classList.remove('hidden');
    terminalOutput.textContent = 'Running code...';
});

closeTerminal.addEventListener('click', () => {
    terminal.classList.add('hidden');
});

socket.on('output', (output) => {
    console.log('Output:', output);
    terminalOutput.textContent = output;
});

function syntax(text) {
    const keywords = {'#eabafe': ['while', 'do', 'end'],'#ffc58f': ['clear'],'#bad9fe': ['incr', 'decr']};
    let highlighted = text.replace(/</g, '&lt;').replace(/>/g, '&gt;');
    for (const [color, words] of Object.entries(keywords)) {
        const regex = new RegExp(`\\b(${words.join('|')})\\b`, 'g');
        highlighted = highlighted.replace(regex, `<span style="color: ${color}">$1</span>`);
    }
    return highlighted;
}

function highlight() {
    const text = code.value;
    overlay.innerHTML = syntax(text);
    overlay.scrollTop = code.scrollTop;
}

code.addEventListener('input', () => {
    highlight();
    updateLineNumbers();
});

code.addEventListener('scroll', () => {
    overlay.scrollTop = code.scrollTop;
    lineNumbers.scrollTop = code.scrollTop;
});

code.addEventListener('keydown', (e) => {
    if (e.key === 'Tab') {
        e.preventDefault();
        const start = code.selectionStart;
        const end = code.selectionEnd;
        code.value = code.value.substring(0, start) + '\t' + code.value.substring(end);
        code.selectionStart = code.selectionEnd = start + 1;
        highlight();
        updateLineNumbers();
    }
});

highlight();
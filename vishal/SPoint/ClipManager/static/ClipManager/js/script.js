function copyCode(button) {
    const code = button.nextElementSibling.innerText;
    navigator.clipboard.writeText(code).then(() => {
        const originalText = button.innerText;
        button.innerText = "Copied!";
        button.style.background = "#27ae60";
        setTimeout(() => {
            button.innerText = originalText;
            button.style.background = "#555";
        }, 2000);
    });
}

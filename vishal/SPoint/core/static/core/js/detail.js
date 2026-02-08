function toggleModal(show) {
    const modal = document.getElementById("customModal");
    if (show) {
        modal.classList.add("show-modal");
    } else {
        modal.classList.remove("show-modal");
    }
}

// Modal ke bahar click karne par close ho jaye
window.onclick = function (event) {
    const modal = document.getElementById("customModal");
    if (event.target == modal) {
        toggleModal(false);
    }
};


// --- Click Toggle Logic (Description Only) ---
document.addEventListener("DOMContentLoaded", () => {
    // Sabhi headings ko select karein
    const headings = document.querySelectorAll(".book-title");

    headings.forEach(heading => {
        heading.addEventListener("click", function () {
            // Heading ke thik baad wala element (Description) select karein
            const desc = this.nextElementSibling;

            // Toggle Display
            if (desc.style.display === "none" || desc.style.display === "") {
                desc.style.display = "block";
            } else {
                desc.style.display = "none";
            }
        });
    });
});

// --- Pagination Logic (Demo) ---
let currentPage = 1;
const nextBtn = document.getElementById("nextBtn");
const prevBtn = document.getElementById("prevBtn");

if (nextBtn) {
    nextBtn.addEventListener("click", () => {
        currentPage++;
        alert("Aap Page " + currentPage + " par ja rahe hain!");
    });
}

if (prevBtn) {
    prevBtn.addEventListener("click", () => {
        if (currentPage > 1) {
            currentPage--;
            alert("Aap Page " + currentPage + " par wapas ja rahe hain!");
        }
    });
}

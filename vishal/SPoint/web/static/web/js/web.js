// --- Sidebar Logic ---
let sidebarOpen = false;
function toggleNav() {
    const sidebar = document.getElementById("mySidebar");
    if (!sidebarOpen) {
        sidebar.style.width = "250px";
        sidebarOpen = true;
    } else {
        sidebar.style.width = "0";
        sidebarOpen = false;
    }
}

// --- Double Tap Logic ---
const heading = document.getElementById("bookHeading");
const desc = document.getElementById("bookDesc");
const content = document.getElementById("bookContent");

heading.addEventListener("dblclick", function () {
    if (desc.style.display === "none" || desc.style.display === "") {
        desc.style.display = "block";
        content.style.display = "none";
    } else {
        desc.style.display = "none";
        content.style.display = "block";
    }
});

// --- Pagination Logic (Demo) ---
let currentPage = 1;
document.getElementById("nextBtn").addEventListener("click", () => {
    currentPage++;
    alert("Aap Page " + currentPage + " par ja rahe hain!");
    // Yahan aap content change karne ka logic add kar sakte hain
});

document.getElementById("prevBtn").addEventListener("click", () => {
    if (currentPage > 1) {
        currentPage--;
        alert("Aap Page " + currentPage + " par wapas ja rahe hain!");
    }
});

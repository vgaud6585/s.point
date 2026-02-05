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

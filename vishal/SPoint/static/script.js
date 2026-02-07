
// --- Sidebar Logic start here ---
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
// --- Sidebar Logic end here ---


// Elements ko select karna
const shape = document.getElementById('shape');
const img = document.getElementById('moving-img');

// Click Event Listener
shape.addEventListener('click', () => {
    
    // 1. Shape ki class toggle karein (Box <-> Circle)
    shape.classList.toggle('circle');
    
    // 2. Image ki position toggle karein (Left <-> Right)
    img.classList.toggle('move-right');

    // 3. Text update karein
    if (shape.classList.contains('circle')) {
        shape.innerText = "CIRCLE";
    } else {
        shape.innerText = "BOX";
    }
});


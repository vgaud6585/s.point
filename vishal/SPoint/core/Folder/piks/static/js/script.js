// Sidebar toggle karne ke liye
function toggleSidebar() {
    const sidebar = document.getElementById("sidebar");
    sidebar.classList.toggle("open");
}

/**
 * Updated function: Ab ye full image dikhane ke saath-saath 
 * niche details (name aur folder) bhi update karega.
 */
function showImageDetails(element) {
    const modal = document.getElementById("imageModal");
    const fullImg = document.getElementById("fullImage");
    
    // UI Elements for details (Jo humne HTML mein add kiye hain)
    const panel = document.getElementById('detailPanel');
    const nameLabel = document.getElementById('dispName');
    const folderLabel = document.getElementById('dispFolder');
    const fullPathLabel = document.getElementById('dispFull');

    // Data attributes se information nikalna
    const src = element.src;
    const fileName = element.getAttribute('data-name');
    const subFolder = element.getAttribute('data-subfolder');

    // 1. Modal mein image dikhana
    modal.style.display = "flex";
    fullImg.src = src;

    // 2. Niche detail panel ko update aur show karna
    if(panel) {
        nameLabel.innerText = fileName;
        folderLabel.innerText = subFolder;
        
        let fullRel = subFolder === "Main Folder" ? fileName : subFolder + "/" + fileName;
        if(fullPathLabel) fullPathLabel.innerText = fullRel;

        panel.classList.remove('d-none'); // Detail panel show karein
        
        // Smooth scroll taaki user ko details dikh jayein
        panel.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }
}

// Purana function compatibility ke liye (agar aap direct src bhej rahe ho kahin se)
function showFullImage(src) {
    const modal = document.getElementById("imageModal");
    const fullImg = document.getElementById("fullImage");
    modal.style.display = "flex";
    fullImg.src = src;
}

// Note box toggle logic
function toggleNoteBox() {
    const box = document.getElementById("floatingNoteBox");
    box.style.display = box.style.display === "block" ? "none" : "block";
}

// Modal ke bahar click karne par close karna
window.onclick = function (event) {
    const modal = document.getElementById("imageModal");
    if (event.target == modal) {
        modal.style.display = "none";
    }
};

// Floating detail box dikhane ke liye
function showFloatingDetails(element) {
    const box = document.getElementById('floatingDetailBox');
    const nameLabel = document.getElementById('dispName');
    const folderLabel = document.getElementById('dispFolder');

    // Data nikalna
    const fileName = element.getAttribute('data-name');
    const subFolder = element.getAttribute('data-subfolder');

    // Content update
    nameLabel.innerText = fileName;
    folderLabel.innerText = subFolder;

    // Box show karna
    box.classList.remove('d-none');
}

// Detail box close karne ke liye
function closeDetailBox() {
    const box = document.getElementById('floatingDetailBox');
    box.classList.add('d-none');
}

// Optional: Agar aap purana Modal bhi use karna chahte hain
function showFullImage(src) {
    const modal = document.getElementById("imageModal");
    const fullImg = document.getElementById("fullImage");
    modal.style.display = "flex";
    fullImg.src = src;
}

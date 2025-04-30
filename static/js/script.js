// A tiny animation when page loads
document.addEventListener("DOMContentLoaded", function() {
    const container = document.querySelector('.container');
    container.style.opacity = 0;
    container.style.transform = "scale(0.9)";
    
    setTimeout(() => {
        container.style.opacity = 1;
        container.style.transform = "scale(1)";
        container.style.transition = "all 0.5s ease";
    }, 100);
});
document.addEventListener('DOMContentLoaded', function () {
    var dimmingText = document.querySelector('.introduction-text');
    var body = document.body;
    
    // Update opacity based on scroll position
    function updateOpacity() {
        var scrollPercentage = window.scrollY / (body.scrollHeight - window.innerHeight);
        var opacity = 1 - scrollPercentage; // Invert the percentage

        // Ensure opacity is between 0 and 1
        opacity = Math.min(1, Math.max(0, opacity));

        dimmingText.style.opacity = opacity.toFixed(2); // Limit decimal places
    }

    // Listen for scroll events
    window.addEventListener('scroll', updateOpacity);
    });
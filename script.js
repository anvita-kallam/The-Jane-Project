// JavaScript for adding interactivity to the navigation

document.addEventListener('DOMContentLoaded', function() {
    // Get all navigation links
    const navLinks = document.querySelectorAll('nav a');

    // Add click event listener to each nav link
    navLinks.forEach(link => {
        link.addEventListener('click', smoothScroll);
    });

    function smoothScroll(e) {
        e.preventDefault();

        const targetId = this.getAttribute('href').substring(1);
        const targetSection = document.getElementById(targetId);

        // Scroll smoothly to the target section
        targetSection.scrollIntoView({
            behavior: 'smooth'
        });

        // Highlight the current active link
        navLinks.forEach(link => {
            link.classList.remove('active');
        });
        this.classList.add('active');
    }
});

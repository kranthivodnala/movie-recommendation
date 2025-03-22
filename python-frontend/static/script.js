document.addEventListener('DOMContentLoaded', function() {
    const slider = document.querySelector('.slider');
    const slideContainer = document.querySelector('.slide-container');
    const slides = document.querySelectorAll('.slide');

    let slideIndex = 0;

    function nextSlide() {
        slideIndex = (slideIndex + 1) % slides.length;
        updateSlide();
    }

    function updateSlide() {
        slideContainer.style.transform = `translateX(-${slideIndex * 100}%)`;
    }

    setInterval(nextSlide, 3000); // Change slide every 3 seconds
});

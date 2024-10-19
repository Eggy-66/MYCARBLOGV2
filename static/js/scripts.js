
    const prevBtn = document.querySelector('.prev-btn');
    const nextBtn = document.querySelector('.next-btn');
    const slides = document.querySelector('.projects-center');
    const totalSlides = document.querySelectorAll('.project').length;
    let slideIndex = 0;

    function updateSlidePosition() {
        const offset = -slideIndex * 100;
        slides.style.transform = `translateX(${offset}%)`;
    }

    prevBtn.addEventListener('click', () => {
        if (slideIndex > 0) {
            slideIndex--;
        } else {
            slideIndex = totalSlides - 1;
        }
        updateSlidePosition();
    });

    nextBtn.addEventListener('click', () => {
        if (slideIndex < totalSlides - 1) {
            slideIndex++;
        } else {
            slideIndex = 0;
        }
        updateSlidePosition();
    });

    // Optional: Auto slide
    setInterval(() => {
        nextBtn.click();
    }, 5000); // Change image every 5 seconds

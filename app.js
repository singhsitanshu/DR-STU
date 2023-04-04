const menu = document.querySelector('#mobile-menu');
const menuLinks = document.querySelector('.navbar__menu');

menu.addEventListener('click', function() {
    menu.classList.toggle('is-active');
    menuLinks.classList.toggle('active');
});

let scrollContainer = document.querySelector(".gallery");
    let backBtn = document.getElementById("backBtn");
    let nextBtn = document.getElementById("nextBtn");

    scrollContainer.addEventListener("wheel", (evt) => {
        evt.preventDefault();
        scrollContainer.scrollLeft += evt.deltaY;
        scrollContainer.style.scrollBehavior = "auto";
    })

    nextBtn.addEventListener("click", ()=> {
        scrollContainer.style.scrollBehavior = "smooth";
        scrollContainer.scrollLeft += 675; // adjust this value as needed
    });
    
    backBtn.addEventListener("click", ()=> {
        scrollContainer.style.scrollBehavior = "smooth";
        scrollContainer.scrollLeft -= 675; // adjust this value as needed
    });    
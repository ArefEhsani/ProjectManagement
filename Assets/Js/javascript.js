/* باز و بسته کردن منوی همبرگری */
function show() {
    const nodeList = document.querySelectorAll(".active-side");


    for (let i = 0; i < nodeList.length; i++) {


        if (nodeList[i].classList.contains('dis')) {
            nodeList[i].classList.remove("dis");
        } else {
            nodeList[i].classList.add("dis");
        }
    }
}

/* اکتیو شدن ایتم های منو */
let navLinks = document.querySelectorAll('.nav-link');

for (let i = navLinks.length; i--;) {
    navLinks[i].addEventListener('click', eventHandler);
}


function eventHandler() {
    this.classList.add('active');
    this.classList.remove('link-dark');
    for (let i = navLinks.length; i--;) {
        if (navLinks[i] != this) navLinks[i].classList.remove('active')
        if (navLinks[i] != this) navLinks[i].classList.add('link-dark')
    }
}
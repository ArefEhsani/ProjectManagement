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
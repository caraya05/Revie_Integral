var elements = document.querySelectorAll(".element");
var colorSelected = document.querySelector("#colorSelected");
var buton = document.querySelector("#login_buton");
var colorx = 0;
let number = [];
var option = {
    animation: true,
    delay: 2000
};


elements.forEach((element) => {
    orden();
    const color = getRandomcolor();
    element.style.backgroundColor = color;
    element.innerHTML = color;
    let nuevo = number.push(color)

});

elements.forEach((element) => {
    element.addEventListener("click", () => {

        return colorx = element.innerHTML;
    });
});

function orden() {
    var rand = Math.floor(Math.random() * number.length);
    console.log(number[rand])
    colorSelected.innerHTML = number[rand];
}

function getRandomcolor() {
    const letter = "0123456789ABCDEF";
    let color = "#";
    var array = [];
    for (let i = 0; i < 6; i++) {
        color += letter[Math.floor(Math.random() * 16)];
    }
    return color;
}

function validar() {
    console.log(colorx);
    console.log("me tengo que ir");
    if (colorx === colorSelected.innerHTML) {
       document.getElementById('formLogi').submit();
    }
    if (colorx != "0") {
        Swal.fire({
                icon: 'warning',
                title: 'Oops...',
                text: 'Recuerda que debes darnos toda la informacion solicitada.'
        })
        return false;
    }
    if (colorx != colorSelected.innerHTML) {
        Swal.fire({
                icon: 'error',
                title: 'Oops...',
                text: 'Vuelve a intentarlo'
        })
        setTimeout(() => {
            location.reload(true)
        }, 10000);

    }
}

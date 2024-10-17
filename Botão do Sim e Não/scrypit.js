

function sim(){
    alert("Tu é mano?");
}

// Adiciona o evento mouseover ao botão "não"
document.getElementById("btnnao").addEventListener("mouseover", function() {
    this.innerText = "Sim";
    this.style.backgroundColor = "lightgreen";
});

// Adiciona o evento mouseout ao botão "não"
document.getElementById("btnnao").addEventListener("mouseout", function() {
    this.innerText = "Não";
    this.style.backgroundColor = "lightcoral";
});
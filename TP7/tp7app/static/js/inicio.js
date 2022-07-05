var contador = 0

function carga() {

    var barra = document.getElementById("carga")
    var iteraciones = document.getElementById("cantIteraciones")
    var cant_ite = iteraciones.value

    if (cant_ite < 100000){
        var total = Math.trunc(cant_ite / 10000)
        console.log(total)
        var a = setInterval(function(){ calcular(a, total, barra)}, 130);

    }
    else{

        var total = Math.trunc(cant_ite / 100000)
        console.log(total)

        var a = setInterval(function(){ calcular(a, total, barra)}, 1120);
    }
}
function calcular(a, total, barra) {
    contador = contador + 1

    var b = (contador*100) / total
    barra.style= "width:"+b+"%"

    if (contador == total){
        borrarAlerta(a)
    }



}
function borrarAlerta(a) {
  clearInterval(a);
}
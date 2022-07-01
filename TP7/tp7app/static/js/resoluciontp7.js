

function pintar(nro, verdesde){

    btn = document.getElementById("btnselec"+nro)
    fila = document.getElementById("filaselec"+nro)

    if (btn.checked) {
        fila.style.backgroundColor="rgb(207, 243, 154)" ;

        for(i=verdesde; i<(verdesde+401); i++){

            if (nro != i)
                filaext = document.getElementById("filaselec"+String(i));
                filaext.style.backgroundColor="white";
            }
        }


}





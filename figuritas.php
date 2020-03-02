<?php
function generarAlbum($capacidad){
    $album=[];
    $numero=0;
    $i=1;
    while ($i <= $capacidad){
        $album[$i]=$numero;
        $i=$i+1;

    }
    return $album;
}

function comprarFigurita($figuritasTotal){
    $figurita = rand(0, $figuritasTotal);
    return $figurita;
}

function rellenarAlbun($tamanoDeAlbum){
    $album = GenerarAlbum();
    $contador=0; 
    while not(estaLleno($album)):
       $figurita=comprarFigurita(f$iguritasTotal)
       $album[$figurita-1]=1
       $contador=$contador+1
    return $contador
$res=cuantasFiguritas($tamanoDeAlbum)
}

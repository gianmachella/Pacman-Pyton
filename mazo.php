<?php
function crear_mazo($n) {
    $mazo = array();
    $k = 0;
    while ($k<$n){
        $i = 1;
        while ($i<=13) {
        $j = 1;
        while ($j <= 4) {
            $mazo[] = $i;
            $j=$j+1;
        }
        $i=$i+1;
        }
        $k = $k+1;
    }
    return $mazo;
}
$mazo = crear_mazo(5);
shuffle($mazos);

function jugar($mazo){
    $i=0;
    $cartas=0;
    while ($i < count($mazo) and $cartas < 21){
        $cartas = $cartas + $mazo[$i];
        array_shift($mazo);
    }   
return $cartas;
}

function jugarVarios($mazo, $jugadores){
    $i = 0;
    $puntos = [];
    while ($i < $jugadores){
        $puntos = jugar($mazo);
        $i=$i+1;
    }
return $puntos;
}

function verQuienGano($puntos){
$i=0;
$resultados=[];
while ($i < count($puntos)){
    if ($puntos[$i] == 21){
        $resultados = 1;
    }else{
        $resultados = 0;
    }
    $i=$i+1;
    }
return $resultados;
}


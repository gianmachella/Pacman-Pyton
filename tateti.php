<?php
function crearTablero($filas, $columnas){
    $tablero=array();
    for ($i=0; $i < $filas; $i=$i+1) { 
        $tablero[$i]=array();
        for ($j=0; $j < $columnas; $j=$j+1) { 
            $tablero[$i][$j]=0;
        }
    }
return $tablero;
}
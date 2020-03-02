<?php

class Billetera {
    private $billetes = array(2=>0, 5=>0, 10=>0, 20=>0, 50=>0, 100=>0, 200=>0, 500=>0, 1000=>0);
    private $totalBilletera=0;

    function agregarPlata($billete, $cantidad){
        if (isset($this->billetes[$billete])){
            $this->billetes[$billete] = $this->billetes[$billete] + $cantidad;
        } else{
            echo "Este valor no corresponde a un billete valido \n";
        }
    }

    function sacarPlata($billete, $cantidad){
        if (isset($this->billetes[$billete])){
        $this->billetes[$billete] = $this->billetes[$billete] - $cantidad;
        } else{
            echo "Este valor no corresponde a un billete valido \n";
        }
    }

    function mostrarPlata(){
        $billetesBilletera = array();
        foreach ($this->billetes as $billete => $valor) {
            if ($valor > 0){
                $billetesBilletera[$billete] = $valor;
            }
        }
        return $billetesBilletera; 
    }

    function totalPlata(){
        foreach($this->billetes as $billete => $cantidad){
            $this->totalBilletera+=($billete * $cantidad);
        }
        echo "Tienes ". $this->totalBilletera. " ". "pesos en total en tu billetera \n";
    }

    function crearBilleteras($cantidadBilleteras){
        $billeteras=[];
        $billetesValor = array(2=>0, 5=>0, 10=>0, 20=>0, 50=>0, 100=>0, 200=>0, 500=>0, 1000=>0);
        $billetes=array_rand($billetesValor);
        $cantidad=rand(1,20);
        $i=0;
        while ( $i<$cantidadBilleteras){
                $billeteras[$i] = new Billetera();
                $j=0;
                $cant=rand(1,9);
                while ($j < $cant){
                    $billetes=array_rand($billetesValor);
                    $cantidad=rand(1,20);
                    $billeteras[$i]->agregarPlata($billetes, $cantidad);
                    $j=$j+1;
                }
            $i=$i+1;
        }
        $this->billetes->mostrarPlata();
        return $billeteras;
    }
}
$billeterasDelSalon=$billeteras->crearBilleteras(15);
print_r($billeterasDelSalon);
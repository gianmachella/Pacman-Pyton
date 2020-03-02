<?php

class Billetera{

    private $billetes=array();

    function agregar($billetes, $cantidad){
        if (!isset($this->billetes[$billetes])){
            $this->billetes[$billetes]=0;
        }
        $this->billetes[$billetes] = $this->billetes[$billetes] + $cantidad;
    }
    function total(){
        $total=0;
        foreach ($this->billetes as $billete => $cantidad) {
            $total = $total + $billete*$cantidad;
        }
        return $total;
    }
    function sacar($billete, $cantidad){
        if (isset($this->billetes[$billete]) && $this->billetes[$billete] >=  $cantidad){
            $this->billetes[$billete] = $this->billetes[$billete] - $cantidad;
        }
    }
}


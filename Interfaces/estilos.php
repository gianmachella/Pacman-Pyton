<?php

include_once 'interfaz.php';

class style implements dibujable
{
    private $listaContenido = array();

    function guardar($contenido)
    {
        $this->listaContenido[] = $contenido;
    }

    public function mostrar()
    {
        echo "<style>";
        foreach($this->listaContenido as $elemento)
        {
            echo $elemento->mostrar(). "\n";
        }
        echo "</style>";
    }
}

class color implements dibujable
{
    private $color;
    private $etiqueta;

    public function __construct($color, $etiqueta)
    {
        $this->color = $color;
        $this->etiqueta = $etiqueta;
    }

    function mostrar()
    {
        echo $this->etiqueta . " {color:$this->color}";
    }
}

class backgroundColor implements dibujable
{
    private $color;
    private $etiqueta;

    public function __construct($color, $etiqueta)
    {
        $this->color = $color;
        $this->etiqueta = $etiqueta;
    }

    function mostrar()
    {
        echo $this->etiqueta . " {background-color:$this->color}";
    }
}
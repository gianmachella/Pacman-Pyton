<?php

include_once 'interfaz.php';

class html implements dibujable
{
    private $listaContenido = array();

    function guardar(dibujable $contenido)
    {
        $this->listaContenido[] = $contenido;
    }

    public function mostrar()
    {
        
        foreach($this->listaContenido as $elemento)
        {
            $elemento->mostrar();
        }
    }
}

class header implements dibujable
{
    private $listaContenido = array();

    function guardar(dibujable $contenido)
    {
        $this->listaContenido[] = $contenido;
    }

    public function mostrar()
    {
        foreach($this->listaContenido as $elemento)
        {
            $elemento->mostrar();
        }
    }
}

class head implements dibujable
{
    private $listaContenido = array();

    function guardar(dibujable $contenido)
    {
        $this->listaContenido[] = $contenido;
    }

    public function mostrar()
    {
        foreach($this->listaContenido as $elemento)
        {
            $elemento->mostrar();
        }
    }
}

class body implements dibujable
{
    private $listaContenido = array();

    function guardar(dibujable $contenido)
    {
        $this->listaContenido[] = $contenido;
    }

    public function mostrar()
    {
        foreach($this->listaContenido as $elemento)
        {
            $elemento->mostrar();
        }
    }
}

class footer implements dibujable
{
    private $listaContenido = array();

    function guardar(dibujable $contenido)
    {
        $this->listaContenido[] = $contenido;
    }

    public function mostrar()
    {
        foreach($this->listaContenido as $elemento)
        {
            $elemento->mostrar();
        }
    }
}

class title implements dibujable
{
    private $contenido;

    public function __construct(string $dato)
    {
        $this->contenido = $dato;
    }

    public function mostrar()
    {
        echo "<title>". $this->contenido. "</title>";
    }
}

class h implements dibujable
{
    private $contenido;
    private $tipo; 

    public function __construct(string $dato, $tipo)
    {
        if ($tipo>=1 and $tipo<=6){
            $this->contenido = $dato;
            $this->tipo = $tipo;
        }
    }

    public function mostrar()
    {
        echo "<h$this->tipo>". $this->contenido. "</h$this->tipo>";
    }
}

class p implements dibujable
{
    private $contenido;

    public function __construct($dato)
    {
        $this->contenido = $dato;
    }

    public function mostrar()
    {
        echo "<p>". $this->contenido. "</p>";
    }
}

class div implements dibujable
{
    private $contenido;

    public function __construct($dato)
    {
        $this->contenido = $dato;
    }

    public function mostrar()
    {
        echo "<div>". $this->contenido. "</div>";
    }
}

class ul implements dibujable
{
    private $contenido;

    public function __construct($dato)
    {
        $this->contenido = $dato;
    }

    public function mostrar()
    {
        echo "<ul>". $this->contenido. "</ul>";
    }
}

class li implements dibujable
{
    private $contenido;

    public function __construct($dato)
    {
        $this->contenido = $dato;
    }

    public function mostrar()
    {
        echo "<li>". $this->contenido. "</li>";
    }
}

class img implements dibujable
{
    private $imagen;

    public function __construct($ubicacion)
    {
        $this->imagen = $ubicacion;
    }

    public function mostrar()
    {
        echo "<img src= $this->imagen>";
    }
}


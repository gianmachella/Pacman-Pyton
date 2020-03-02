<?php

include 'interfaz.php';

class Container implements Mostrable 
{

    private $capacidad;
    private $capacidadUtilizada = 0;
    private $capacidadRestante;
    private $contenido = array();

    public function __construct($capacidad)
    {
        $this->capacidad = $capacidad;
        $this->capacidadRestante = $capacidad;
    }

    public function guardar(guardable $objeto)
    {
        if ($objeto->volumen() <= $this->capacidadRestante)
        {
            $this->contenido[] = $objeto; 
            $this->capacidadRestante = $this->capacidadRestante - $objeto->volumen();
            $this->capacidadUtilizada= $this->capacidadUtilizada + $objeto->volumen();
            return True;
        }
        return False;
    }

    public function mostrar(){
        foreach($this->contenido as $elemento) 
        {
            $elemento->mostrar();
        }
    }

    public function totalDeContenido() 
    {
        return count($this->contenido);
    }

    public function capacidadRestante()
    {
        echo "Quedan ". $this->capacidadRestante. "litros de capacidad\n";
    }

    public function capacidadUtilizada()
    {
        echo "Haz utilizado ". $this->capacidadUtilizada. "litros de capacidad de la capacidad total\n";
    }

}

class Auto implements Mostrable, Guardable
{
    private $dimenciones;

    public function __construct($dimenciones)
    {
        $this->dimenciones = $dimenciones;
    }

    public function volumen()
    {
        return $this->dimenciones;
    }

    public function mostrar() 
    {
        echo "Auto\n";
    }
}

class Bici implements Mostrable, Guardable 
{
    private $dimenciones;

    public function __construct($dimenciones)
    {
        $this->dimenciones = $dimenciones;
    }

    public function volumen()
    {
        return $this->dimenciones;
    }

    public function mostrar() 
    {
        echo "Bici\n";
    }
}
class Camioneta implements Mostrable, Guardable 
{
    private $dimenciones;

    public function __construct($dimenciones)
    {
        $this->dimenciones = $dimenciones;
    }

    public function volumen()
    {
        return $this->dimenciones;
    }

    public function mostrar() 
    {
        echo "Camioneta\n";
    }
}

///Medidas:
///Container=76351410
///Auto=11441760
///Bici=2050

$container = new Container(76351410);
$megane = new Auto(11441760);
$pinarello = new Bici(200050);
$SW4 = new Camioneta(19348760);

if ($container->guardar($megane)==False)
{
    echo "No se pudo guardar este ". $objeto->mostrar(). "por que ya no queda espacio en este Container";
}

if ($container->guardar($SW4)==False)
{
    echo "No se pudo guardar este ". $objeto->mostrar(). "por que ya no queda espacio en este Container";
}

if ($container->guardar($SW4)==False)
{
    echo "No se pudo guardar este ". $objeto->mostrar(). "por que ya no queda espacio en este Container";
}

if ($container->guardar($SW4)==False)
{
    echo "No se pudo guardar este ". $objeto->mostrar(). "por que ya no queda espacio en este Container";
}

if ($container->guardar($pinarello)==False)
{
    echo "No se pudo guardar este ". $objeto->mostrar(). "por que ya no queda espacio en este Container";
}
if ($container->guardar($pinarello)==False)
{
    echo "No se pudo guardar este ". $objeto->mostrar(). "por que ya no queda espacio en este Container";
}

if ($container->guardar($pinarello)==False)
{
    echo "No se pudo guardar este ". $objeto->mostrar(). "por que ya no queda espacio en este Container";
}

if ($container->guardar($pinarello)==False)
{
    echo "No se pudo guardar este ". $objeto->mostrar(). "por que ya no queda espacio en este Container";
}

if ($container->guardar($pinarello)==False)
{
    echo "No se pudo guardar este ". $objeto->mostrar(). "por que ya no queda espacio en este Container";
}

if ($container->guardar($megane)==False)
{
    echo "No se pudo guardar este ". $objeto->mostrar(). "por que ya no queda espacio en este Container";
}


$container->mostrar();
$container->capacidadUtilizada();
$container->capacidadRestante();
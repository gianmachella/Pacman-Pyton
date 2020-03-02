<?php

require_once("./vendor/autoload.php");
require_once("Billetera.php");

use PHPUnit\Framework\TestCase;
final class billeteraTest extends TestCase
{
    function testExisteBilletera(){
        $billetera = new Billetera();
        $this->assertTrue(!empty($billetera));
    }

    function testAgregarBilletes(){
        $billetera = new Billetera;
        $billetera->agregar(100,5);
        $this->assertTrue(True);
    }

    function testTieneTotal(){
        $billetera = new Billetera;
        $total=$billetera->total();
        $this->assertTrue(True);
    }

    function testAgregarBilletesYVerificarTotal(){
        $billetera = new Billetera();
        $billetera->agregar(100,5);
        $total=$billetera->total();
        $this->assertEquals(500, $total);
    }

    function testAgregarDosVeces(){
        $billetera = new Billetera;
        $billetera->agregar(100,5);
        $billetera->agregar(20,10);
        $total = $billetera->total();
        $this->assertEquals(700, $total);
    }

    function testAgregarDosVecesLoMismo(){
        $billetera = new Billetera();
        $billetera->agregar(100,5);
        $billetera->agregar(100,5);
        $total=$billetera->total();
        $this->assertEquals(1000, $total);
    }

    function testexisteSacar(){
        $billetera = new Billetera();
        $billetera->sacar(100,1);
        $total = $billetera->total();
        $this->assertEquals(0, $total);
    }

    function testAgregarYSacar(){
        $billetera = new Billetera;
        $billetera->agregar(100,5);
        $billetera->sacar(100,1);
        $total = $billetera->total();
        $this->assertEquals(400, $total);
    }

    function testSacarDosVeces(){
        $billetera = new Billetera;
        $billetera->agregar(100,5);
        $billetera->sacar(100,1);
        $billetera->sacar(100,1);
        $total = $billetera->total();
        $this->assertEquals(300, $total);
    }

    function testSacarMasDeLoQueTenemos(){
        $billetera = new Billetera;
        $billetera->agregar(100,5);
        $billetera->sacar(100,6);
        $total = $billetera->total();
        $this->assertEquals(500, $total);
    }

}
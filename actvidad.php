<?php
/**
 * =====================================
 * 1 - Cuanto vale $a en los tres casos:
 * =====================================
 */
//a
$a = 10;
function ej1_a() {
  $a = 11;
}
ej1_a();
//a=10

//b
$b = 10;
function ej1_b() {
  global $b;
  $b = 11;
}
ej1_b();
//$b = 11

//c
$c = 10;
function ej1_c() {
  $c = 11;
  global $c;
}
ej1_c();
//$c = 10

//d
$d = 10;
function ej1_d() {
  global $d;
  $d = 11;
}
//$d = 11

//e
$e = 11;
function ej1_e1() {
  ej1_e2();
  $e = 12;
}
function ej1_e2() {
  global $e;
}
ej1_e1();
//$e = 11


/**
 * =====================================
 * 2 - imprimir secuencias con bucles
 * =====================================
 */
//a - Escribir un bucle for y un while donde se
//    imprimen solo los valores impares desde 0 a 20

for ($i=1; $i <= 20; $i=$i+2) { 
    echo $i, "\n";
}

$i=1;
while ($i <= 20) {
    echo $i, "\n";
    $i=$i+2;
}


//b - Igual al punto a pero en orden inverso salteando de a uno
//    (imprime la mitad de numeros)

for ($i=19; $i >= 0; $i=$i-4) { 
    echo $i, "\n";
}

$i=19;
while ($i >= 0) {
    echo $i, "\n";
    $i=$i-4;
}

//c - Crear un arreglo de 10 elementos y recorrerlo
//    con un foreach en ambos sentidos
//    (hint: puede usar funciones de array antes de entrar al foreach)

$numeros = array();
for ($i=1; $i <= 10; $i++) { 
    $numeros[$i] = $i;
}

foreach ($numeros as $numero) {
    echo $numero, "\n";
}

foreach (array_reverse($numeros)as $numero) {
    echo $numero, "\n";
}

//d - Crear un arreglo de 10 elementos y recorrerlo de ambos sentidos
//    con un for y un while

$numeros = array();
for ($i=1; $i <= 10; $i++) { 
    $numeros[$i] = $i;
}

for ($i=1; $i <= count($numeros); $i++) { 
    echo $numeros[$i], "\n";
}

$i=1;
while ($i <= count($numeros)) {
    echo $numeros[$i], "\n";
    $i++;
}

/**
 * =====================================
 * 3 - Arreglos
 * =====================================
 */
//a - Crear un arreglo de una dimensión de mil elementos
//    con claves consecutivas

$numeros = array();
for ($i=1; $i <= 1000; $i++) { 
    $numeros[$i] = $i;
}

//b - Crea un arreglo de 100elementos con claves numericas pero pares
//    Ej: $a[0], $a[2], $a[3] deben existir, $a[1], $a[3] no deben existir

$numeros = array();
for ($i=0; $i <= 200; $i=$i+2) { 
    $numeros[$i] = $i;
}

//c - Si nos pasan un arreglo y no sabemos el contenido, cual suele ser la mejor
//    forma de recorrerlo? Se puede de más formas?

//La mejor forma para recorrer un arreglo es con un Foreach, hay otras formas, como un For o While//
 
/**
 * =====================================
 * 4 - funciones
 * =====================================
 */
//a - Crear una funcion que dado un arreglo/array duplica todos los valores

$ar = array(1, 2, 3);
function ej4_a($ar){
    foreach ($ar as $k =>$valor) {
        $ar[$k] = $valor*2;
    }
    return $ar;
}
ej4_a($ar);



//b - Crea una funcion que dado un arreglo/array te devuelve un nuevo arreglo
//    con los valores duplicados pero no modifica el original (debe crear un
//    nuevo arreglo)

$ar = array(1, 2, 3);
$newArray = array();
function createNewArray($ar, $newArray){
    for ($i=0; $i < count($ar); $i++) { 
        $newArray[$i] = $ar[$i]*2;
    }
    return $newArray;
}
createNewArray($ar, $newArray);

//c - De un ejemplo de función recursiva

function restarNumero($num){
    echo $num, "\n";
 
    if($num>0){
        restarNumero(--$num);
    }
}
restarNumero(10);

//d - En este psuedo codigo, puede decirme si anda si lo programaramos en PHP?
//    Que devuelve? Que estamos calculando?
/**

f1( $var1 ) {
  if $var1 > 1{
    return $var1 * f2($var1 - 1)
  }
  return $var1
}
f2( $var2 ) {
  if $var2 > 1{
    return $var2 * f1($var2 - 1)
  }
  return $var2
}
f1(5) // cuanto devuelve?
      // que esta calculando?
//////////////////////////////////////////////////
function f1($var1) {
    if ($var1 > 1){
      return $var1 * f2($var1-1);
    }
    return $var1;
  }
  function f2($var2) {
    if ($var2 > 1){
      return $var2 * f1($var2-1);
    }
    return $var2;
  }
$prueba=f1(5);

print_r($prueba);

      SI ANDA PROGRMADO EN PHP
      DEVUELVE 120
      ESTA CALCULANDO UN FACTORIAL DE UN NUMERO (PUDO USARSE UNA FUNCION RECURSIVA, ES UN BUEN EJEMPLO PARA USARSE)
*/
/**
 * =====================================
 * 5 - A desarrollar
 * =====================================
 */
//a - Arregle el siguiente codigo

$a = array(1,2,3);
$b = array(4,5,6);

echo "Las keys del arreglo a son: \n";

foreach ($a as $k => $v) {
  echo $k . "\n";
}
echo "\n\n";
// duplico todos los elementos sin agregar nuevos
foreach ($b as $k => $v) {
  $b[$k] = $v*2;
}
echo $v . "\n";
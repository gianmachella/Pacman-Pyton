<?php

$a = array(1,2,3);
$b = array(4,5,6);

echo "Las keys del arreglo a son: \n";

foreach ($a as $k => $v) {
  echo $k . "\n";
}
echo "\n\n";
// duplico todos los elementos sin agregar nuevos
foreach ($a as $k => $v) {
  $b[$v] = $v*2;
}
echo $v . "\n";
//print_r($prueba);
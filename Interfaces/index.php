<?php

include "clases.php";
include "estilos.php";

$html = new html();
$header = new header();
$title = new title("Academia Hitss");
$body = new body();
$h1 = new h ("Academia Hitss", 1);
$img = new img ("/academia.jpeg");
$p = new p("Estos son los integrantes de la 2da. edición de la Academia PHP de Global Hits");
$footer = new footer("Gian Machella");
$style = new style();
$background = new backgroundColor("gray", "body");

$html->guardar($header);
$header->guardar($title);
$html->guardar($body);
$body->guardar($h1);
$body->guardar($img);
$body->guardar($p);
$html->guardar($footer);
$header->guardar($style);
$style->guardar($background);

$html->mostrar();
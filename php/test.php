<?php
$fin = fopen( 'input.txt', 'r' );
$fout = fopen('output.txt' , 'w');


$stroka = "10 + - 2";
$rezultat=eval("return $stroka;");
echo $rezultat;

fclose( $fout);
fclose( $fin);
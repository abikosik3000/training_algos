<?php
$fin = fopen( 'input.txt', 'r' );
$fout = fopen('output.txt' , 'w');


var_dump(strlen('Тест'));
//$k = (int)trim(fgets($fin));
//$string = trim(fgets($fin));
//$a = explode(" " , trim(fgets($fin)));


//fputs($fout, $max_now_combo);

fclose( $fout);
fclose( $fin);
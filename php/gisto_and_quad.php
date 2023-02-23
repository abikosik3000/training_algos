<?php
function print_arr($a){
    echo "\n";
    foreach($a as $k => $el){
        echo "$k->$el ";
    }
    echo "\n";
}

$fin = fopen( 'input.txt', 'r' );
$fout = fopen('output.txt' , 'w');

//$n = (int)trim(fgetss($fin));
$gisto = explode( " ", trim(fgets($fin)));
$n = $gisto[0];
$gisto = array_slice($gisto , 1);
//print_arr($gisto);


$stak = array();
$max_s = 0;
foreach($gisto as $c){

    //print_arr($stak);
    //echo " now $c";

    if(count($stak) == 0){
        $stak[$c] = 1;
        continue;
    }

    //vitalkivaem bolshie
    $last_val = 0;
    if(array_key_last($stak) > $c){
        while( count($stak) > 0){
            $last_key = array_key_last($stak);
            $last_val += array_pop($stak);
            $max_s = max( $max_s , (int)$last_val * (int)$last_key );
    
            $last_key = array_key_last($stak);
            if(isset($last_key) && $last_key <= $c){
                //$stak[$last_key] += $last_val;
                break;
            }
        }
    }

    if( array_key_last($stak) < $c){
        $stak[$c] = 1 + $last_val;
        continue;
    }
    if( array_key_last($stak) == $c){
        $stak[$c] += 1 + $last_val;
        continue;
    }
}

$last_val = 0;
while( count($stak) > 0){
    $last_key = array_key_last($stak);
    $last_val += array_pop($stak);
    $max_s = max( $max_s , (int)$last_val * (int)$last_key );
}

fputs($fout, $max_s);

fclose( $fout);
fclose( $fin);
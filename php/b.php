<?php
$fin = fopen( 'input.txt', 'r' );
$fout = fopen('output.txt' , 'w');

$k = (int)trim(fgets($fin));
$string = trim(fgets($fin));



$chars = array();
for($i = 97 ; $i < 123; $i++){
    $chars[] = chr($i);
}


$max_now_combo = 0;

foreach( $chars as $search_char){
    //echo $search_char;

    $now_kombo = 0;
    $now_can_replace = (int)$k;
    $start = 0;

    if(strpos($string, $search_char) === false){
        continue;
    }

    for($i_now = 0 , $n = strlen( $string) ; $i_now < $n ; $i_now++){
        $now_char = $string[$i_now];

        
        
        //echo "repl " . $now_can_replace . "  " .$now_char."\n";

        if($now_char != $search_char){
            
            if($now_can_replace > 0 ){
                $now_can_replace--;
            }
            else{
                while(true){

                    if($n - 1 == $start){
                        break;
                    }
                    $start++;
                    if($string[$start - 1] != $search_char){
                        break;
                    }
                };
            }
        }
        
        //echo "$start $i_now\n";
        $now_kombo = $i_now - $start + 1;
        $max_now_combo = max($max_now_combo ,$now_kombo);
        
    }
}


fputs($fout, $max_now_combo);



fclose( $fout);
fclose( $fin);
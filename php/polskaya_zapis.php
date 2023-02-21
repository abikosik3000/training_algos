<?php
$fin = fopen( 'input.txt', 'r' );
$fout = fopen('output.txt' , 'w');

$in_s = trim(fgets($fin));
$infiks_w = array();

$num_buff = '';
for($i = 0 ; $i <  strlen( $in_s ) ; $i++){

    $now_char = $in_s[$i];
    
    if( is_numeric( $now_char) ){
        $num_buff .= $in_s[$i];
        
    }
    else{
        
        if($num_buff != ''){
            
            $infiks_w[] = (int)$num_buff;
            $num_buff = '';
        }
        
        if($now_char != ' '){
            $infiks_w[] = $now_char;
        }
    }
    
}


$stak = array();
$postfix_w = array();

class Operation{

    public function __construct( public $priority, public $make_operation, public $need_vars = 2){}

};

$operations = [
    "-" => new Operation(1, fn($x_arr) => $x_arr[1] - $x_arr[0] ),
    "+" => new Operation(1, fn($x_arr) => $x_arr[1] + $x_arr[0] ),
    "*" => new Operation(2, fn($x_arr) => $x_arr[1] * $x_arr[0] ),
];

for($i = 0 ; $i < count($infiks_w) ; $i++ ){

    $now_char = $infiks_w[$i];
    

    if(is_numeric( $now_char)){
        $postfix_w[] = $now_char;
        continue;
    }

    if($now_char == "("){
        $stak[] = $now_char;
        continue;
    }

    if($now_char == ")"){

        while(count($stak) > 0){

            if(end($stak) == "("){
                array_pop($stak);
                break;
            }
            $postfix_w[] = array_pop($stak);
        }
        continue;
    }

    if(isset( $operations[$now_char] )){

        while(count($stak) > 0){
            if(end($stak) == "("){
                break;
            }
            if( $operations[$now_char]?->priority > $operations[end($stak)]?->priority){
                break;
            }
            $postfix_w[] = array_pop($stak);
            
        }
        $stak[] = $now_char;
        continue;
    }
}


while(count($stak) > 0){
    $postfix_w[] = array_pop($stak);
}

$stak = array();
foreach( $postfix_w as $now_char){
    if(is_numeric($now_char)){
        $stak[] = $now_char;
    }
    if(isset($operations[$now_char])){
        $operands = array();
        for($i = 0;$i < $operations[$now_char]->need_vars ; $i++){
            $operands[] = array_pop($stak);
        }
        $stak[] = ($operations[$now_char]->make_operation)($operands);
    }

}

//var_dump($stak);
echo 1+(2*6 - 3) - 3 *(3- 4) ;

fputs($fout, end($stak));

fclose( $fout);
fclose( $fin);
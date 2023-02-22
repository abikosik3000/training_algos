<?php

class Operation{
    public function __construct( public $priority, public $make_operation, public $need_vars = 2){}
};

function chek_skobe_balans($in_s)
{
    $balanse = 0;
    for($i = 0 ; $i <  strlen( $in_s ) ; $i++){
        $now_char = $in_s[$i];
        if($now_char == "("){
            $balanse++;
        }
        if($now_char == ")"){
            $balanse--;
            if($balanse < 0 ){
                return false;
            }
        }
    }
    return $balanse == 0;
}

function chek_correct_infix($infiks_w)
{
    //global $operations;
    if(count( $infiks_w ) == 0){
        return true;
    }
    $last_num = is_numeric($infiks_w[0]);
    for($i = 1 ; $i <  count( $infiks_w ) ; $i++){
        if( $infiks_w[$i] == "("  || $infiks_w[$i] == ")"){
            continue;
        }
        $now_num = is_numeric($infiks_w[$i]);
        if($now_num == $last_num && $now_num == true){
            return false;
        }
        $last_num = $now_num;
    }

    return true;
}


function calc_to_array($in_s , &$infiks_w){

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
            if($now_char != ' '){ $infiks_w[] = $now_char; }
        }
    }
    if($num_buff != ''){
        $infiks_w[] = (int)$num_buff;
        $num_buff = '';
    }
}


$operations = [
    "!" => new Operation(10, fn($x_arr) => !$x_arr[0] ,1),
    "&" => new Operation(3, fn($x_arr) => $x_arr[1] && $x_arr[0] ),
    "|" => new Operation(2, fn($x_arr) => $x_arr[1] || $x_arr[0] ),
    "^" => new Operation(2, fn($x_arr) => $x_arr[1] xor $x_arr[0] ),
];

function infiks_to_postfix($infiks_w , &$postfix_w){
    $stak = array();
    $postfix_w = array();

    global $operations;
    
    foreach($infiks_w as $now_char){

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
}

function calc_postfix($postfix_w){
    $stak = array();

    global $operations;

    foreach( $postfix_w as $now_char){
        if(is_numeric($now_char)){
            $stak[] = $now_char;
        }
        if(isset($operations[$now_char])){
            $operands = array();
            for($i = 0;$i < $operations[$now_char]->need_vars ; $i++){
                if(count($stak) == 0){
                    return "WRONG";
                }
                $operands[] = array_pop($stak);
            }
            $stak[] = ($operations[$now_char]->make_operation)($operands);
        }
        //var_dump($stak);
    }
    

    if(sizeof($stak) == 1){
        return (int)$stak[0];
    }
    else{
        return "WRONG";
    }
}

function print_arr($a){
    echo "\n";
    foreach($a as $el){
        echo "$el ";
    }
    echo "\n";
}

$fin = fopen( 'input.txt', 'r' );
$fout = fopen('output.txt' , 'w');


$in_s = trim(fgets($fin));

$infiks_w = array();
$postfix_w = array();
if( chek_skobe_balans($in_s) ){

    calc_to_array($in_s , $infiks_w);
    if(chek_correct_infix($infiks_w)){
        //print_arr($infiks_w );
        infiks_to_postfix($infiks_w , $postfix_w);
        //print_arr($postfix_w);

        
        fputs($fout,calc_postfix($postfix_w));
    }
    else{
        fputs($fout,"WRONG");
    }
}
else{
    fputs($fout,"WRONG");
}



fclose( $fout);
fclose( $fin);
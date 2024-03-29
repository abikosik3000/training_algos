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
    //два числа подряд
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

function print_arr($a){
    echo "\n";
    foreach($a as $el){
        echo "$el ";
    }
    echo "\n";
}

function calc_to_array($in_s , &$infiks_w){

    $num_buff = '';
    for($i = 0 ; $i <  strlen( $in_s ) ; $i++){
        $now_char = $in_s[$i];

        if( $now_char =="." || is_numeric( $now_char)  || ord($now_char) >= 97 && ord($now_char) <= 122){
            $num_buff .= $in_s[$i];
        }
        else{
            if($num_buff != ''){
                //write numeric
                $infiks_w[] = $num_buff;
                $num_buff = '';
            }
            if($now_char != ' '){ 
                //write operand
                if( $now_char == "-" && 
                ( !is_numeric(end($infiks_w)) || count($infiks_w) == 0)  ){
                    $now_char = "~";
                }
                $infiks_w[] = $now_char; 
            }
        }
    }
    if($num_buff != ''){
        $infiks_w[] = $num_buff;
        $num_buff = '';
    }
}

$operations = [
    "~" => new Operation(10, fn($x_arr) => 0 - $x_arr[0] ,1),
    "/" => new Operation(3, function($x_arr) {
        if($x_arr[0] == 0){
            throw new Exception("Деление на ноль", 1);
        }  
        return $x_arr[1] / $x_arr[0];
    }
),
    "*" => new Operation(3, fn($x_arr) => $x_arr[1] * $x_arr[0] ),
    "+" => new Operation(2, fn($x_arr) => $x_arr[1] + $x_arr[0] ),
    "-" => new Operation(2, fn($x_arr) => $x_arr[1] - $x_arr[0] ),
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
                    throw new Exception("Ошибка представления", 1);
                }
                $operands[] = array_pop($stak);
            }
            $stak[] = ($operations[$now_char]->make_operation)($operands);
        }
    }
    
    if(sizeof($stak) == 1){
        return $stak[0];
    }
    else{
        throw new Exception("Ошибка представления", 1);
    }
}

$fin = fopen( 'input.txt', 'r' );
$fout = fopen('output.txt' , 'w');

$in_s = trim(fgets($fin));
$replace = [];

//$stdin = fopen('php://stdin', 'r');
echo "переменые из файла?[Y/n]\n";
$from_file = trim(fgets(STDIN));

if($from_file == "n"){
    for($i = 0; $i < strlen($in_s) ; $i++){
        if(preg_match('/[a-z]/' , $in_s[$i])){
            if(isset($replace[$in_s[$i]]  ) === false){
                $number = 0;
                echo "{$in_s[$i]} =\n";
                $number = trim(fgets(STDIN));
                $replace[$in_s[$i]] = $number;
            }
        }
    }
}
else{
    while(true){
    
        $in = fgets($fin);
        
        if($in === false){
            break;
        }
        $in = explode(" ",trim($in) );
        $replace[$in[0]] = $in[1];
    }
}

function podstanovka(&$s , $repl){
    foreach($repl as $k => $v){
        $s =str_replace($k,$v,$s);
    }
}

function approve($stroka){
    $rezultat=eval("return $stroka;");
    return $rezultat;
}

$infiks_w = array();
$postfix_w = array();
if( chek_skobe_balans($in_s) ){

    podstanovka($in_s , $replace);
    calc_to_array($in_s , $infiks_w);

    if(chek_correct_infix($infiks_w)){
         
        infiks_to_postfix($infiks_w , $postfix_w);
        try{
            $rez_calc = calc_postfix($postfix_w);
            fputs($fout,"выражение $in_s \n");
            fputs($fout,"результат $rez_calc \n");
            $rez_approve = approve($in_s);
            fputs($fout,"проверка $rez_approve \n");
        }
        catch(Exception $e){
            echo 'Выброшено исключение: ',  $e->getMessage(), "\n";
        }
    }
    else{
        fputs($fout,"Несколько переменных подряд");
    }
}
else{
    fputs($fout,"Ошибка скобочной последовательности");
}

fclose( $fout);
fclose( $fin);

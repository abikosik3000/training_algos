<?php

function swipesWithSum($sum){
    $res = [];
    for($i = 0 ; $i <= $sum;$i++){
        $res[] = [$i, $sum - $i];
    }
    return $res;
}

function printWithPostfix($total_sum , $postfix){
    
    $swipes = swipesWithSum($total_sum - $postfix);
    foreach($swipes as $x){
        print(extract($x).$postfix."\n");
    }
}

function main_f(){

    for($i = 3; $i < 1000 ; $i= $i  +3 ){
        if($i % 5 != 0){
            if(($i % 10) + (int)($i / 10 ) % 10 + (int)($i / 100) % 10 < 10){
                print($i);
            }
        }
    }
}

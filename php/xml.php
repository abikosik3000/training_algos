<?php

function xml_to_array($s){
    $res = [];
    $buff = "";
    for($i = 0; $i < strlen($s) ; $i++){
        $ch = $s[$i];
        $buff .= $ch;

        if($ch == ">"){
            $res[] = $buff;
            $buff = "";
        }
    }
    return $res;
}

function chek_skobes($s){
    $total_blocks = 0;
    $balnse = 0;
    for($i = 0; $i < strlen($s) ; $i++){
        $ch = $s[$i];
        
        if($ch == "<"){
            $balnse++;
        }
        if($ch == ">"){
            $balnse--;
            $total_blocks++;
        }
        if(abs($balnse) > 1 ){
            return false;
        }
        if($balnse == 0 && $ch != ">"){
            return false;
        }
    }
    return $balnse == 0 && $total_blocks > 1;
}

function chek_xml_correct($a){
    $stak = [];
    foreach($a as $v){
        if(strlen($v) < 3){
            return false;
        }
        if($v[1] != "/"){
            $stak[] = $v;
            continue;
        }
        if($v[1] == "/"){
            if(strlen($v) < 4){
                return false;
            }
            if(count($stak) == 0){
                return false;
            }
            $v = str_replace("/","",$v);
            if( array_pop($stak) != $v){
                return false;
            }
            continue;
        }
    }
    return (count($stak) == 0);
}

function find_pare($a , &$p1 , &$p2){
    $not_paired = [];
    foreach($a as $i => $v){
        if($v[1] != "/"){
            $not_paired[$v] = $i;
        }
    }
    print_arr($not_paired);
    foreach($a as $i => $v){
        if($v[1] == "/"){
            $v_open = str_replace("/" ,"",$v);
            if(isset($not_paired[$v_open])){
                unset($not_paired[$v_open]);
            }
            else{
                $not_paired[$v] = $i;
            }
        }
    }
    print_arr($not_paired);
    $p2 = array_pop($not_paired);
    $p1 = array_pop($not_paired);
}

function try_connect_pair(&$a , $p1 , $p2){
    $a_copy = $a;
    if($a[$p2][1] != "/"){
        $a_copy[$p2][1] = "/";
        if(chek_xml_correct($a_copy)){
            $a = $a_copy;
            return true;
        }
        return false;
    }
    $t1 = substr($a[$p1], 1 ,-1);
    $t2 = substr($a[$p2], 2 ,-1);
    if(strlen($t1) != strlen($t2)){
        return false;
    }
    $index_diff = null;
    for($i = 0; $i < strlen($t1) ; $i++){
        if($t1[$i] !=  $t2[$i]){
            if($index_diff !== null){
                return false;
            }
            $index_diff = $i;
        }
    } 
    if($t2[$index_diff] != "X" && $t2[$index_diff] != "/"){
        $t1[$index_diff] = $t2[$index_diff];
    }
    $t2[$index_diff] = $t1[$index_diff];
    $a_copy[$p1] = "<{$t1}>";
    $a_copy[$p2] = "</{$t2}>";
    if(chek_xml_correct($a_copy)){
        $a =$a_copy;
        return true;
    }else{
        return false;
    }
}

function pair_main( $s ){
    global $fout;
    if(!chek_skobes($s)){
        return false;
    }
    $a = xml_to_array($s);
    if(chek_xml_correct($a)){
        fputs($fout, implode("", $a));
        exit;
    }
    for($i = 0; $i < count($a); $i++){
        for($j = $i + 1; $j < count($a); $j++){
            if(try_connect_pair($a,$i ,$j)){
                fputs($fout, implode("", $a));
                exit;
            }
        }
    }
}

$fin = fopen( 'input.txt', 'r' );
$fout = fopen('output.txt' , 'w');
$s = trim(fgets($fin));
if(chek_skobes($s)){
    pair_main( $s );
}
else{
    $count_open = substr_count($s ,"<");
    $count_close = substr_count($s ,">");
    $diiferent = abs($count_open - $count_close);
    $repl_to = ($count_open <= $count_close) ? "<" : ">";
    $repl_from = ($count_open <= $count_close) ? ">" : "<";

    if($diiferent == 1){
        for($i = 0; $i < strlen($s) ; $i++){
            $s_copy = $s;
            $s_copy[$i] = "X";
            pair_main( $s_copy );
            
            $s_copy[$i] = $repl_to;
            if(chek_skobes($s_copy)){
                $tegs_copy = xml_to_array($s_copy);
                if(chek_xml_correct($tegs_copy)){
                    fputs($fout, implode("", $tegs_copy));
                    exit;
                }
            }
        }
    }

    if($diiferent == 2){
        $s_copy = "";
        for($i = 0; $i < strlen($s) ; $i++){
            if($s[$i] != $repl_from){
                continue;
            }
            $s_copy = $s;
            $s_copy[$i] = $repl_to;
            
            if(chek_skobes($s_copy)){
                $tegs_copy = xml_to_array($s_copy);
                if(chek_xml_correct($tegs_copy)){
                    fputs($fout, implode("", $tegs_copy));
                    exit;
                }
            }
        }
    }
}
fclose( $fout);
fclose( $fin);
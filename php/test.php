<?php
/*
$fin = fopen( 'input.txt', 'r' );
$fout = fopen('output.txt' , 'w');

$gisto = explode( " ", trim(fgets($fin)));
$n = $gisto[0];
$gisto = array_slice($gisto , 1);*/



class Node{
    public $left = null;
    public $right = null;
    public $val;

    public function __construct($val= null){
        $this->val = $val;
    }
}

function ebka($root){

    $q = [$root];
    while(count($q) > 0){
        $now_node = array_pop($q);
        if(is_null($now_node)){
            continue;
        }

        //SWAP
        $buff = $now_node->left;
        $now_node->left = $now_node->right;
        $now_node->right = $buff;

        $q[] = $now_node->left;
        $q[] = $now_node->right;

    }

    return $root;
}
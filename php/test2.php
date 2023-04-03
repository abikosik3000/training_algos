<?php
/*
$fin = fopen( 'input.txt', 'r' );
$fout = fopen('output.txt' , 'w');

$gisto = explode( " ", trim(fgets($fin)));
$n = $gisto[0];
$gisto = array_slice($gisto , 1);*/

use Heap as GlobalHeap;

class Heap{

    private $arr = [];
    private $comparator;
    public $last_add_ind = null;
    public $last_add_ind2 = null;

    public function __construct($comparator = null){
        if($comparator === null){
            $this->comparator = fn($x,$y) => $x <= $y;
        }
        else{
            $this->comparator = $comparator ;
        }
    }

    public function peek(){
        return $this->arr[0];
    }

    public function count(){
        return count($this->arr);
    }

    public function print(){
        echo "\n";
        foreach($this->arr as $k => $el){
            echo "$el ";
        }
        echo "\n";
    }
    
    public function heapify($a){
        $this->arr = $a;
        for($i = intdiv($this->count() ,2) ; $i >= 0 ;$i-- ){
            $now_ind = $i;
            while(true){
                $parent_ind = $this->parent_ind($now_ind);
                if( $parent_ind  < 0){
                    break;
                }
                if( ($this->comparator)($this->arr[$parent_ind] ,  $this->arr[$now_ind])  ){
                    break;
                }
                $parent_ind = $this->parent_ind($now_ind);
                //swipe
                $buff =  $this->arr[$parent_ind];
                $this->arr[$parent_ind] =  $this->arr[$now_ind];
                $this->arr[$now_ind] = $buff;
                $now_ind = $parent_ind;
            }
        }
        //TODO
    }

    private function parent_ind($i){ 
        return intdiv($i - 1,2);
    }
    private function soon1_ind($i){ 
        return 2 * $i + 1;
    }
    private function soon2_ind($i){ 
        return 2 * $i + 2;
    }

    public function add($new_el){
        $this->arr[] = $new_el;
        $now_ind = array_key_last( $this->arr);
        while(true){
            $parent_ind = $this->parent_ind($now_ind);
            if($parent_ind < 0){
                break;
            }
            if(  ($this->comparator)($this->arr[$parent_ind] ,  $this->arr[$now_ind])  ){
                break;
            }

            //swipe
            $buff =  $this->arr[$parent_ind];
            $this->arr[$parent_ind] =  $this->arr[$now_ind];
            $this->arr[$now_ind] = $buff;
            $now_ind = $parent_ind;
        }
    }

    public function pop(){

        $ret = $this->arr[0];
        $this->arr[0] = end($this->arr);
        $now_index = 0;
        while($this->soon2_ind($now_index) < count($this->arr)){
            $min_soon_ind = $this->soon2_ind($now_index);
            if( ($this->comparator)($this->arr[$min_soon_ind - 1] , $this->arr[$min_soon_ind])){
                $min_soon_ind = $min_soon_ind - 1;
            }

            if(($this->comparator)($this->arr[$now_index] , $this->arr[$min_soon_ind])){
                break;
            }
            
            //swipe
            $buff = $this->arr[$min_soon_ind];
            $this->arr[$min_soon_ind] = $this->arr[$now_index];
            $this->arr[$now_index] = $buff;
            $now_index = $min_soon_ind;
        }
        array_pop($this->arr);
        return $ret;
    }
}



function f($arrays){

    $heap = new Heap();
    for($i =0 ;$i < count($arrays);)
        if( ! empty($arr)){
            $heap->add([
                'value' => $arr[0],
                'pos_element' => 0,
                'num_array' => $i
            ]);
        }
    
    $answ = [];
    while($heap->count() > 0){
        $boof = $heap->pop();
        $answ[] = $boof['value'];
        if(isset($arrays[ $boof['num_array']][$boof['pos_element'] + 1])){
            $heap->add(
                $arrays[ $boof['num_array']][$boof['pos_element'] + 1]

            );
        }
    }//sorted set



}
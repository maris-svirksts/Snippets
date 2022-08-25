<?php
class Node{
    public $data;
    public $next;
    function __construct($d)
    {
        $this->data = $d;
        $this->next = NULL;
    }
}
class Solution{

	function removeDuplicates($head){
        $list       = array();
        $returnHead = null;
        $newList    = new Solution();

        while($head) {
            $list[] = $head->data;
            $head   = $head->next;
        }

        $filteredList = array_unique( $list );

        foreach( $filteredList as $element ) {
            $returnHead = $newList->insert( $returnHead, $element );
        }

        return $returnHead;
    }

    function insert( $head, $data ){
       $p = new Node( $data );

       if( $head == null ){
            $head = $p;
       }  
       else if( $head->next == null ){
            $head->next = $p;
       } 
       else{
            $start = $head;

            while( $start->next != null ){
                    $start = $start->next;
            }
            $start->next = $p;
       }
       
       return $head;
    }

    function display($head){
        $start=$head;
        while($start){
           echo $start->data,' ';
           $start=$start->next;
        }
    }
}
$T=intval(fgets(STDIN));
$head=null;
$mylist=new Solution();
while($T-->0){
    $data=intval(fgets(STDIN));
    $head=$mylist->insert($head,$data);
}
$head=$mylist->removeDuplicates($head);
$mylist->display($head);
?>

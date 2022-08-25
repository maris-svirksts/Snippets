<?php
// https://www.hackerrank.com/challenges/30-binary-trees/tutorial
class Node{
    public $left,$right;
    public $data;
    function __construct($data)
    {
        $this->left=$this->right=null;
        $this->data = $data;
    }
}
class Solution{
    public function insert($root,$data){
        if($root==null){
            return new Node($data);
        }
        else{            
            if($data<=$root->data){
                $cur=$this->insert($root->left,$data);
                $root->left=$cur;
            }
            else{
                $cur=$this->insert($root->right,$data);
                $root->right=$cur;
            }
            return $root;
        }
    }

	public function levelOrder($root){
        $list = [];
        self::levelOrderLoop($root, 0, $list);

        foreach($list as $elements) {
            foreach($elements as $element) {
                echo $element;
                echo ' ';
            }
        }
    }

    private function levelOrderLoop($root, $location, &$list) {
        if( ! $root ) { return; }
        
        $current_depth = count($list);

        if( $current_depth <= $location ) {
            array_push($list, []);
        }
        array_push($list[$location], $root->data);

        self::levelOrderLoop($root->left, $location + 1, $list);
        self::levelOrderLoop($root->right, $location + 1, $list);
    }

}//End of Solution
$myTree=new Solution();
$root=null;
$T=intval(fgets(STDIN));
while($T-->0){
    $data=intval(fgets(STDIN));
    $root=$myTree->insert($root,$data);
}
$myTree->levelOrder($root);
?>

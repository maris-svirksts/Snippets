<?php
// Challenge of discutable value.

$handle = fopen ("php://stdin","r");
fscanf($handle,"%s",$S);

$result = ( is_numeric( $S ) == true ) ? $S : 'Bad String';

echo $result;
?>
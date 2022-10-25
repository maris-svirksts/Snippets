<?php
/**
 * https://www.codingame.com/ide/puzzle/telephone-numbers
 **/

fscanf(STDIN, "%d", $N);
$elements = array();

for ($i = 0; $i < $N; $i++) {
    fscanf(STDIN, "%s", $telephone);

    for($y = 0; $y < strlen($telephone); $y++) {
        $elements[substr($telephone, 0, $y + 1)] = 0;
    }
}

echo( count($elements) . "\n");
?>
<?php
/**
 * https://www.codingame.com/ide/puzzle/1d-spreadsheet
 **/

function calculate($key) {
    // global - bad practice.
    global $dict;
    $result = null;

    if(is_numeric($key)) {
        return $key;
    } else if('VALUE' == $dict[$key][0]) {
        $value = calculate($dict[$key][1]);
        return $value;
    } else if('ADD' == $dict[$key][0]){
        $result = calculate($dict[$key][1]) + calculate($dict[$key][2]);
    } else if ('SUB' == $dict[$key][0]) {
        $result = calculate($dict[$key][1]) - calculate($dict[$key][2]);
    } else if ('MULT' == $dict[$key][0]) {
        $result = calculate($dict[$key][1]) * calculate($dict[$key][2]);
    }

    $dict[$key] = array('VALUE', $result, '_');
    return $result;
}

$dict = array();

fscanf(STDIN, "%d", $N);
for ($i = 0; $i < $N; $i++) {
    fscanf(STDIN, "%s %s %s", $operation, $arg1, $arg2);
    $dict['$' . $i] = array($operation, $arg1, $arg2);
}

for ($i = 0; $i < $N; $i++) {
    echo calculate('$' . $i) . "\n";
}
?>
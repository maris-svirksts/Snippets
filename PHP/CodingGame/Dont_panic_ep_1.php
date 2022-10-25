<?php
/**
 * https://www.codingame.com/ide/puzzle/don't-panic-episode-1
 **/

function block($clonePos, $exitPos, $direction) {
    $action = 'WAIT';

    if(($clonePos > $exitPos && $direction == 'RIGHT') || ($clonePos < $exitPos && $direction == 'LEFT')) {
        $action = 'BLOCK';
    }

    return $action;
}

// $nbFloors: number of floors
// $width: width of the area
// $nbRounds: maximum number of rounds
// $exitFloor: floor on which the exit is found
// $exitPos: position of the exit on its floor
// $nbTotalClones: number of generated clones
// $nbAdditionalElevators: ignore (always zero)
// $nbElevators: number of elevators
fscanf(STDIN, "%d %d %d %d %d %d %d %d", $nbFloors, $width, $nbRounds, $exitFloor, $exitPos, $nbTotalClones, $nbAdditionalElevators, $nbElevators);

$elevator = array();

for ($i = 0; $i < $nbElevators; $i++) {
    // $elevatorFloor: floor on which this elevator is found
    // $elevatorPos: position of the elevator on its floor
    fscanf(STDIN, "%d %d", $elevatorFloor, $elevatorPos);
    $elevator[$elevatorFloor] = $elevatorPos;
}

// game loop
while (TRUE) {
    // $cloneFloor: floor of the leading clone
    // $clonePos: position of the leading clone on its floor
    // $direction: direction of the leading clone: LEFT or RIGHT
    fscanf(STDIN, "%d %d %s", $cloneFloor, $clonePos, $direction);

    if($cloneFloor == $exitFloor) {
        $action = block($clonePos, $exitPos, $direction);
    } else {
        $action = block($clonePos, $elevator[$cloneFloor], $direction);
    }

    echo($action . "\n"); // action: WAIT or BLOCK
}
?>
/**
 * https://www.codingame.com/ide/puzzle/don't-panic-episode-1
 **/

function block(clonePos, exitPos, direction) {
    let action = 'WAIT';

    if((clonePos > exitPos && direction == 'RIGHT') || (clonePos < exitPos && direction == 'LEFT')) {
        action = 'BLOCK';
    }

    return action;
}

var inputs                  = readline().split(' ');
const nbFloors              = parseInt(inputs[0]); // number of floors
const width                 = parseInt(inputs[1]); // width of the area
const nbRounds              = parseInt(inputs[2]); // maximum number of rounds
const exitFloor             = parseInt(inputs[3]); // floor on which the exit is found
const exitPos               = parseInt(inputs[4]); // position of the exit on its floor
const nbTotalClones         = parseInt(inputs[5]); // number of generated clones
const nbAdditionalElevators = parseInt(inputs[6]); // ignore (always zero)
const nbElevators           = parseInt(inputs[7]); // number of elevators

let elevator = [];

for (let i = 0; i < nbElevators; i++) {
    let inputs = readline().split(' ');
    elevator[parseInt(inputs[0])] = parseInt(inputs[1]); // floor => position on which this elevator is found.
}

// game loop
while (true) {
    /**
     * cloneFloor: floor of the leading clone
     * clonePos: position of the leading clone on its floor
     * direction: direction of the leading clone: LEFT or RIGHT
     **/

    let [cloneFloor, clonePos, direction] = readline().split(' ');

    cloneFloor = parseInt(cloneFloor);
    clonePos   = parseInt(clonePos);

    if(cloneFloor == exitFloor) {
        action = block(clonePos, exitPos, direction);
    } else {
        action = block(clonePos, elevator[cloneFloor], direction);
    }


    console.log(action); // action: WAIT or BLOCK

}

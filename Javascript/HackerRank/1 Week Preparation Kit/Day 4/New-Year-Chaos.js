'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the 'minimumBribes' function below.
 *
 * The function accepts INTEGER_ARRAY q as parameter.
 */

function minimumBribes(arr) {
    let bribes = 0;
    let expected = [1, 2, 3];

    for (const element of arr) {
        if( expected.includes(element) ) {
            bribes += expected.indexOf(element);

            expected.push(expected.slice(-1).pop() + 1);
            expected.splice(expected.indexOf(element), 1);
        } else {
            console.log('Too chaotic');
            return;
        }
    }
    
    console.log(bribes);
}

function main() {
    const t = parseInt(readLine().trim(), 10);

    for (let tItr = 0; tItr < t; tItr++) {
        const n = parseInt(readLine().trim(), 10);

        const q = readLine().replace(/\s+$/g, '').split(' ').map(qTemp => parseInt(qTemp, 10));

        minimumBribes(q);
    }
}

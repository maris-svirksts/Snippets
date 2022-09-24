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
 * 
 * NOTE: current solution needs to be optimized to complete all test cases.
 */

function minimumBribes(arr) {
    let n       = arr.length - 1;
    let counter = 0;

    let sorted = arr.slice().sort(function(a, b) { return a - b; });
    
    for (let i = 0; i <= n; i++) {
        for (let j = 0; j < n - i; j++) {
            if(arr[j] - j - 1 > 2) {
                console.log('Too chaotic');
                return;
            } else if( sorted != arr ) {
                if (arr[j] > arr[j + 1]) {
                    let temp   = arr[j];
                    arr[j]     = arr[j + 1];
                    arr[j + 1] = temp;

                    counter++;
                }
            }
        }
    }

    console.log(counter);
}

function main() {
    const t = parseInt(readLine().trim(), 10);

    for (let tItr = 0; tItr < t; tItr++) {
        const n = parseInt(readLine().trim(), 10);

        const q = readLine().replace(/\s+$/g, '').split(' ').map(qTemp => parseInt(qTemp, 10));

        minimumBribes(q);
    }
}

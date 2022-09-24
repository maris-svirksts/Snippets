'use strict';

const fs = require('fs');

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
 * Complete the 'palindromeIndex' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts STRING s as parameter.
 */

function palindromeIndex(s) {
    // Write your code here
    let half   = Math.floor(s.length / 2);
    let start  = s.slice(0, half);
    let end    = s.slice(0 - half).split('').reverse().join('');

    if(start === end){
        return -1;
    } else {
        let position = 0;

        while(position < start.length){
            if(start[position] != end[position]){
                break;
            }
            position++;
        }

        let edit_start = start.split('');
        let edit_end   = end.split('');
        let middle     = s[half];

        edit_start.splice(position, 1);
        edit_end.splice(position, 1);

        edit_start = edit_start.join('') + middle;
        edit_end   = edit_end.join('') + middle;

        if(start === edit_end){
            return s.length - position - 1;
        } else if(edit_start === end){
            return position;
        } else {
            return -1;
        }
    }
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const q = parseInt(readLine().trim(), 10);

    for (let qItr = 0; qItr < q; qItr++) {
        const s = readLine();

        const result = palindromeIndex(s);

        ws.write(result + '\n');
    }

    ws.end();
}

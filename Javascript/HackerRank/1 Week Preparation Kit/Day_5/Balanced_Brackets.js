// https://www.hackerrank.com/interview/preparation-kits/one-week-preparation-kit/one-week-day-five/challenges

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
 * Complete the 'isBalanced' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING s as parameter.
 */

function isBalanced(s) {
    while(true) {
        let initial_lenght = s.length;

        s = s.replace("()", '');
        s = s.replace("[]", '');
        s = s.replace("{}", '');

        if(s.length == initial_lenght){
            break;
        }
    }
    
    if(s.length == 0){
        return "YES";
    } else{
        return "NO";
    }
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const t = parseInt(readLine().trim(), 10);

    for (let tItr = 0; tItr < t; tItr++) {
        const s = readLine();

        const result = isBalanced(s);

        ws.write(result + '\n');
    }

    ws.end();
}
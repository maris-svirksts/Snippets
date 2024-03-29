// https://www.hackerrank.com/interview/preparation-kits/one-week-preparation-kit/one-week-day-three/challenges

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
 * Complete the 'caesarCipher' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts following parameters:
 *  1. STRING s
 *  2. INTEGER k
 */

function caesarCipher(s, k) {
    // Write your code here
    let alphabet  = 'abcdefghijklmnopqrstuvwxyz';
    let translate = s.split('');

    let result = translate.map(function(x) {
        let is_upper   = x.toUpperCase() === x ? true : false;
        let index      = alphabet.indexOf(x.toLowerCase());
        let translated = index >= 0 ? alphabet[(index + k) % (alphabet.length)] : x;

        return is_upper === true ? translated.toUpperCase() : translated;
    });
    
    return result.join('');
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const n = parseInt(readLine().trim(), 10);

    const s = readLine();

    const k = parseInt(readLine().trim(), 10);

    const result = caesarCipher(s, k);

    ws.write(result + '\n');

    ws.end();
}

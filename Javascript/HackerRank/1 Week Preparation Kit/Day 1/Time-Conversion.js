// https://www.hackerrank.com/interview/preparation-kits/one-week-preparation-kit/one-week-day-one/challenges

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
 * Complete the 'timeConversion' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING s as parameter.
 */

function timeConversion(s) {
    let hour  = s.slice(0, 2);
    let am_pm = s.slice(-2);

    if (am_pm == 'AM' && hour == '12') { hour = '00'; }
    else if(am_pm == 'PM' && hour != '12') { hour = parseInt(hour) + 12; }

    return hour + s.slice(2, -2);
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const s = readLine();

    const result = timeConversion(s);

    ws.write(result + '\n');

    ws.end();
}

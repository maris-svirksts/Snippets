// https://www.hackerrank.com/interview/preparation-kits/one-week-preparation-kit/one-week-day-two/challenges

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
 * Complete the 'lonelyinteger' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER_ARRAY a as parameter.
 */

function lonelyinteger(a) {
    // Write your code here
    a.sort();
    
    if(a.length == 1){ return a[0]; }
    else{
        let result = a[0];
  
        while(a.length > 1){
            if(result != a[1]){
                return result;
            } else {
                a      = a.filter(function(e) { return e !== a[1] });
                result = a[0];                
            }
        }
        
        return a[0];
    }
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const n = parseInt(readLine().trim(), 10);

    const a = readLine().replace(/\s+$/g, '').split(' ').map(aTemp => parseInt(aTemp, 10));

    const result = lonelyinteger(a);

    ws.write(result + '\n');

    ws.end();
}

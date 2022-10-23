/**
 * https://www.codingame.com/ide/puzzle/1d-spreadsheet
 **/

 const N = parseInt(readline());

 function calculate(key) {
     let result = null;
     let value;

     if(!isNaN(key)) {
         return parseInt(key);
     } else if('VALUE' == dict[key][0]) {
         value = calculate(dict[key][1]);
         return value;
     } else if('ADD' == dict[key][0]){
         result = calculate(dict[key][1]) + calculate(dict[key][2]);
     } else if ('SUB' == dict[key][0]) {
         result = calculate(dict[key][1]) - calculate(dict[key][2]);
     } else if ('MULT' == dict[key][0]) {
         result = calculate(dict[key][1]) * calculate(dict[key][2]);
     }

     // While -0 === 0, there is a test on CodingGame that fails because of that.
     if(result == -0) {
        result = 0;
     }
 
     dict[key] = ['VALUE', result, '_'];
     return result;
 }
 
 let dict = {};
 
 for (let i = 0; i < N; i++) {
     dict['$' + i] = readline().split(' ');
 }
 
 for (let i = 0; i < N; i++) {
     console.log(calculate('$' + i));
 }
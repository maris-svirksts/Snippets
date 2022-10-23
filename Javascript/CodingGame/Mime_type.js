/**
 * https://www.codingame.com/ide/puzzle/mime-type
 **/

 const N = parseInt(readline()); // Number of elements which make up the association table.
 const Q = parseInt(readline()); // Number Q of file names to be analyzed.
 
 let dict = {};
 
 for (let i = 0; i < N; i++) {
     var inputs = readline().split(' ');
     dict[inputs[0].toLowerCase()] = inputs[1];
 }
 
 for (let i = 0; i < Q; i++) {
     let data = readline().split('.'); // One file name per line.
 
     if(1 == data.length) {
         console.log("UNKNOWN");
     } else {
         // For each of the Q filenames, display on a line the corresponding MIME type. If there is no corresponding type, then display UNKNOWN.
         let results = data[data.length - 1].toLowerCase() in dict ? dict[data[data.length - 1].toLowerCase()] : "UNKNOWN";
         console.log(results);
     }
 }
 
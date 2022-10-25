/**
 * https://www.codingame.com/ide/puzzle/telephone-numbers
 **/

 const N        = parseInt(readline());
 const elements = new Set()
 
 for (let i = 0; i < N; i++) {
     const telephone = readline();
 
     for (let y = 0; y < telephone.length; y++) {
         elements.add(telephone.substring(0, y + 1));
     }
 }
 
 console.log(elements.size);
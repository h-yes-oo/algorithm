const fs = require("fs");
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const num = parseInt(input[0]);

// let set = new Set();
// for(let i = 1; i < num + 1; i++){
//   if(!set.has(input[i])){
//     set.add(input[i]);
//   }
// }

input.splice(0,1);
input.splice(-1,1);
let answer = input.filter((value, index) => input.indexOf(value) === index);

answer.forEach((word, index) => console.log(word))
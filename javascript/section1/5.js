const fs = require("fs");
const input = fs.readFileSync('/dev/stdin').toString().split(' ');

let min = parseInt(input[0]);
for(let i = 1; i < input.length; i++){
  if(parseInt(input[i]) < min) min = parseInt(input[i]);
}

console.log(min);
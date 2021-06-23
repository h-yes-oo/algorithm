const fs = require("fs");
const input = fs.readFileSync('/dev/stdin').toString().split('\n')[0];

let result = '';
for(let letter of input){
  if(!isNaN(letter)) result += letter;
}

console.log(parseInt(result));

const sol = input.replace(/[^0-9]/g,'');
console.log(parseInt(sol));
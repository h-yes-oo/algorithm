const fs = require("fs");
const input = fs.readFileSync('/dev/stdin').toString().split('\n')[0];

let set = new Set();
let sol = '';

for(let letter of input){
  if(!set.has(letter)) {
    set.add(letter);
    sol += letter;
  }
}

console.log(sol);
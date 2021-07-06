const fs = require("fs");
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const first = input[0];
const second = input[1];

function sol(long, short){
  let count = 0;
  for(let letter of long){
    if(letter === short){
      count += 1;
    }
  }
  return count;
}

console.log(sol(first, second));
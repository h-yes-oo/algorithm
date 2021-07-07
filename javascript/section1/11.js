const fs = require("fs");
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const string = input[0];

function sol(str){
  let count = 0;
  for(let letter of str){
    if(letter.toUpperCase() === letter){
      count += 1;
    }
  }
  return count;
}

console.log(sol(string));
const fs = require("fs");
const input = fs.readFileSync('/dev/stdin').toString().split('\n')[0];

function sol(str){
  let result = '';
  for(let letter of str){
    if(letter.toUpperCase() === letter) result += letter.toLowerCase();
    else result += letter.toUpperCase();
  }
  return result;
}

console.log(sol(input));
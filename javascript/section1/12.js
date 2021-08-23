const fs = require("fs");
const input = fs.readFileSync('/dev/stdin').toString().split('\n')[0];

function sol(str){
  let result = '';
  for(let letter of str){
    result += letter.toUpperCase();
  }
  return result;
}

console.log(sol(input));

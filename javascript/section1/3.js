const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split(' ');
let a = parseInt(input[0]);

function solution(a) {
  let sol = Math.ceil(a/12);
  return sol;
}

console.log(solution(a));
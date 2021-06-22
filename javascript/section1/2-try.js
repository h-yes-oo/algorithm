const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split(' ');
let a = parseInt(input[0]);
let b = parseInt(input[1]);
let c = parseInt(input[2]);

const triangle = (a,b,c) => {
  if (a+b > c) return "NO";
  else if (a+c > b) return "NO";
  else if (b+c > a) return "NO";
  else return "YES";
}

console.log(triangle(a,b,c));
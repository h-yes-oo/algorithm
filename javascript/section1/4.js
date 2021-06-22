const fs = require("fs");
const input = fs.readFileSync('/dev/stdin').toString().split(' ');
const a = parseInt(input[0]);

let sol = 0;
for(let i = 1; i <= a; i++){
  sol += i;
}
console.log(sol);
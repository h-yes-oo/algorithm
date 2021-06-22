const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split(' ');
let a = parseInt(input[0]);

const sum = (n) => {
  let total = n;
  for(let i = 1; i < n; i++){
    total += i;
  }
  return total;
}

console.log(sum(a));


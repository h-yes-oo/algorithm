const fs = require("fs");
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const [n,m] = input[0].split(' ').map(x => parseInt(x));
const list = input[1].split(' ').map(x => parseInt(x));

let start = 0;
let sum = 0;

for(let i = 0; i < m; i++){
  sum += list[i];
}

let result = sum;

for(let end = m; end < n; end++){
  sum += list[end];
  sum -= list[start++];
  result = Math.max(sum, result);
}

console.log(result);
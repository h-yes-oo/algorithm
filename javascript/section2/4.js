const fs = require("fs");
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const num = parseInt(input[0]);
const score = input[1].split(' ').map(x => parseInt(x));

for (let idx = 1; idx < num; idx++){
  if(score[idx] === 1) score[idx] += score[idx-1];
}

console.log(score.reduce((acc, value) => acc + value, 0));
const fs = require("fs");
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const num = parseInt(input[0]);
const score = input[1].split(' ').map(x => parseInt(x));

const result = Array.from({length: num}, (v, i) => 1);

for(let idx = 0; idx < num; idx++){
  for(let comp = 0; comp < num; comp++){
    if(score[comp] > score[idx]) result[idx]++;
  }
}

const print = result.join(' ');
console.log(print);
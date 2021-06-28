const fs = require("fs");
const input = fs.readFileSync('/dev/stdin').toString().split(' ');

const harr = input.map(x => Number(x));

function solution(harr){
  let sum = harr.reduce((a,b) => a+b, 0) - 100;
  for(let i = 0; i < 9; i++){
    for(let j = i + 1; j < 9; j++) {
      if(harr[i] + harr[j] === sum){
        harr.splice(j, 1);
        harr.splice(i, 1);
        return harr;
      }
    }
  }
  return [];
}

const sol = solution(harr);
sol.forEach((val) => process.stdout.write(`${val} `));
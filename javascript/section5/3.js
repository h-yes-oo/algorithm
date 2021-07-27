const fs = require("fs");
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const [n,m] = input[0].split(' ').map(x => parseInt(x));
const list = input[1].split(' ').map(x => parseInt(x));


let answer = 0;
for(let start = 0; start < n; start++){
  let sum = 0;
  let end = start;
  while(sum < m && end < n){
    sum += list[end++];
    if(sum === m) answer++;
  }
}

console.log(answer);
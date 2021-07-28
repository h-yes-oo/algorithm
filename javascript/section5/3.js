const fs = require("fs");
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const [n,m] = input[0].split(' ').map(x => parseInt(x));
const list = input[1].split(' ').map(x => parseInt(x));

function sol1(n,m, list){
  let answer = 0;
  for(let start = 0; start < n; start++){
    let sum = 0;
    let end = start;
    while(sum < m && end < n){
      sum += list[end++];
      if(sum === m) answer++;
    }
  }
  return answer;
}

function sol2(n, m, list){
  let answer = 0;
  let sum = 0;
  let start = 0;
  for(let end = 0; end < n; end++){
    sum += list[end];
    if(sum === m) answer++;
    while(sum >= m){
      sum -= list[start++];
      if(sum === m) answer++;
    }
  }
  return answer;
}

console.log(sol1(n,m,list));
console.log(sol2(n,m,list));
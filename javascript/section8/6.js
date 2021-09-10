"use strict";
// get input
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const [limit, num] = input[0].split(' ').map(x => Number(x));
const list = [];
for(let idx = 1; idx < num+1; idx++){
  list.push(Number(input[idx]));
}

const sol = (limit, num, list) => {
  const dogs = list.slice().sort((a,b) => a-b);
  let answer = -1;
  const DFS = (level, sum) => {
    if(sum > limit) return;
    if(level === num){
      answer = Math.max(answer, sum);
      return;
    }
    DFS(level+1, sum);
    DFS(level+1, sum+dogs[level]);
  }
  DFS(0,0);
  console.log(answer);
  return;
}

sol(limit, num, list);


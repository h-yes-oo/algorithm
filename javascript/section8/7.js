"use strict";
// get input
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const [num, limit] = input[0].split(' ').map(x => Number(x));
const list = [];
for(let idx = 1; idx < num + 1; idx++){
  const [x,y] = input[idx].split(' ').map(x => Number(x));
  list.push([x,y]);
}

const sol = (num, limit, list) => {
  let maxScore = -1;
  const DFS = (level, score, time) => {
    if(time < 0) return;
    if(level === num){
      maxScore = Math.max(maxScore, score);
      return;
    }
    // 이걸 풀었을 때
    DFS(level+1, score + list[level][0], time - list[level][1]);
    // 이걸 안 풀었을 때
    DFS(level+1, score, time);
  }
  DFS(0,0,limit);
  console.log(maxScore);
  return;
}

sol(num, limit, list);

/*
5 20
10 5
25 12
15 8 
6 3 
7 4
*/

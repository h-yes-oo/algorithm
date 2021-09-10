"use strict";
// get input
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const num = Number(input[0]);
const list = input[1].split(' ').map(x => Number(x));

const sol = (num, list) => {
  const goal = list.reduce((a,b) => a+b, 0) / 2;
  let answer = false;
  const DFS = (level, sum) => {
    if(level === num) {
      if(sum === goal) answer = true;
      return;
    }
    if(answer) return;
    DFS(level+1, sum);
    DFS(level+1, sum + list[level]);
  }
  DFS(0,0);
  if(answer) console.log('YES');
  else console.log('NO');
}

sol(num, list);

/*
6
1 3 5 6 7 10
*/
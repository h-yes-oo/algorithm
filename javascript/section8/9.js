"use strict";
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const num = Number(input[0]);
const type = input[1].split(' ').map(x => Number(x));
const money = Number(input[2]);

const sol = (num, type, money) => {
  const types = type.slice();
  let minimum = Number.MAX_SAFE_INTEGER;
  const DFS = (level, remain) => {
    if(level >= minimum) return;
    if(remain === 0) minimum = Math.min(minimum,level);
    else if(remain < 0) return;
    else {
      for(let idx = 0; idx < num; idx++){
        DFS(level+1, remain - types[idx]);
      }
    }
  }
  DFS(0,money);
  console.log(minimum);
}

sol(num, type, money);

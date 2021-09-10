"use strict";
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const num = Number(input[0]);

const sol = (num) => {
  const DFS = (level) => {
    if(level === 1) return 1;
    else return level * DFS(level-1);
  }
  let ans = DFS(num);
  console.log(ans);
};

sol(num);
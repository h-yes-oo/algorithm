"use strict";
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const [n, m] = input[0].split(' ').map(x => Number(x));

const sol = (n,m) => {
  let tmp = Array.from({length: m}, () => 0);
  let ans = [];
  const DFS = (level, last) => {
    if(level === m){
      ans.push(tmp.join(' '));
    } else {
      for(let i = last; i < n+1; i++){
        tmp[level] = i;
        DFS(level + 1, i+1);
      }
    }
  };
  DFS(0, 1);
  console.log(ans.join('\n'));
};

sol(n,m);

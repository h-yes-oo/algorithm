"use strict";
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const [n,m] = input[0].split(' ').map(x => Number(x));
const list = input[1].split(' ').map(x => Number(x));

const sol = (n, m, list) => {
  let answer = [];
  let check = Array.from({length: n}, () => 0);
  let tmp = Array.from({length: m}, () => 0);
  const DFS = (level) => {
    if(level === m) answer.push(tmp.join(' '));
    else {
      for(let i = 0; i < n; i++){
        if(check[i] === 0){
          check[i] = 1;
          tmp[level] = list[i];
          DFS(level+1);
          check[i] = 0; 
        }
      }
    }
  }
  DFS(0);
  console.log(answer.join('\n'));
  console.log(answer.length);
};

sol(n, m, list);
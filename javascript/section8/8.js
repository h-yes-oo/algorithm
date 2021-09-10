"use strict";
// get input
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const [n, m] = input[0].split(' ').map(x => Number(x));

const sol = (n,m) => {
  let ans = [];
  const DFS = (level, sum) => {
    if(level === m) {
      ans.push(sum);
      return;
    } else {
      for(let x = 1; x <= n; x++){
        DFS(level+1, sum +`${x} `);
      }
    }
  }
  DFS(0, '');
  console.log(ans.join('\n'));
};

sol(n,m);
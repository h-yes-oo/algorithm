"use strict";
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const num = Number(input[0]);
const list = input[1].split(' ').map(x => Number(x));

// 2 7 5 8 6 4 7 12 3
// 1 2 2 3 3 2 4 5

const sol = (num, list) => { 
  let memo = Array.from({length: num}, () => 0);
  for(let idx = 0; idx < num; idx++){
    let ans = 1;
    for(let bidx = 0; bidx < idx; bidx++){
      if(list[bidx] < list[idx]) ans = Math.max(ans, memo[bidx] + 1);
    }
    memo[idx] = ans;
  }
  console.log(Math.max(...memo));
}

sol(num, list);
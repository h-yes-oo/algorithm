"use strict";
// get input
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const num = Number(input[0]);

// 4 = 100
// 4 / 2 = 2 ... 0
// 2 / 2 = 1 ... 0
// 1 / 2 = 0 ... 1

// 7 = 111
// 7 / 2 = 3 ... 1
// 3 / 2 = 1 ... 1
// 1 / 2 = 0 ... 1
const sol = (n) => {
  let ans = [];
  const binary = (n) => {
    if(n === 0) return;
    binary(parseInt(n/2));
    ans.push(n%2);
  }
  binary(n);
  console.log(ans.join(''));
}

sol(num);
"use strict";
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const num = Number(input[0]);
const height = input[1].split(' ').map(x => Number(x));

let answer = [];
let sorted = height.slice().sort();
for(let idx = 0; idx < num-1; idx++){
  if(sorted[idx] != height[idx]){
    answer.push(idx + 1);
  }
}

console.log(answer.join(' '))

// 120 130 *150* 150 *130* 150
// 120 *150* 130 130 *130*
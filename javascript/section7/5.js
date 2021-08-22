"use strict";
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const [size, num] = input[0].split(' ').map(x => Number(x));
const work = input[1].split(' ').map(x => Number(x));

let count = 0;
let result = [];
for(let idx = num - 1; idx >= 0 && count < size; idx--){
  let x = work[idx];
  if(!result.includes(x)) {
    count++;
    result.push(x);
  }
}
console.log(result.join(' '));

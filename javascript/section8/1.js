"use strict";
// get input
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const num = Number(input[0]);

let array = [];

// print(3) -> print(2) -> print(1) -> print(2) -> print(3)

const print = (n) => {
  if(n > 1) print(n-1);
  array.push(n);
}

print(num);
console.log(array.join(' '));
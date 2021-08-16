"use strict"
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const [n, k] = input[0].split(' ').map(x => Number(x));

const sol = (n,k) => {
  let stack = Array.from({length: n}, (v, i) => i+1);
  let order = 1;
  while(stack.length > 1){
    let current = stack.shift()
    if(order < k) {
      stack.push(current);
      order++;
    }
    else order = 1;
  }
  console.log(stack[0]);
}

const betterSol = (n,k) => {
  let stack = Array.from({length: n}, (v, i) => i+1);
  while(stack.length > 1){
    for(let order = 1; order < k; order++){
      stack.push(stack.shift());
    }
    stack.shift();
  }
  console.log(stack[0]);
}

sol(n, k);
betterSol(n, k);
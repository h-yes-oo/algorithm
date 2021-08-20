"use strict"
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const [norm, course] = input;

const sol = (norm, course) => {
  let queue = [];
  for(let x of norm) queue.push(x);
  for(let y of course){
    if(y === queue[0]) queue.shift();
    if(queue.length === 0) return 'YES';
  }
  return 'NO';
}

const betterSol = (norm, course) => {
  let queue = norm.split('');
  for(let y of course){
    if(queue.includes(y)) 
      if(queue.shift() !== y) return 'NO';
  }
  if(queue.length > 0) return 'NO';
  return 'YES';
}

console.log(sol(norm, course));
console.log(betterSol(norm, course));
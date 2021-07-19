"use strict";
const fs = require("fs");
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const num = parseInt(input[0]);
const board = [];
const input2 = input.splice(1,num);
input2.forEach((value, index) => board.push(
  value.split(' ').map(x => parseInt(x))
  )
);

let max = 0;

board.forEach((value, idx) => {
  const rowTotal = value.reduce((acc, val) => acc + val, 0);
  if(rowTotal > max) max = rowTotal;
});

for(let col = 0; col < num; col++){
  let colTotal = 0;
  for(let row = 0; row < num; row++){
    colTotal += board[row][col];
  }
  if(colTotal > max) max = colTotal;
};

let crossTotal = 0;
for(let idx = 0; idx < num; idx++){
  crossTotal += board[idx][idx];
};

if(crossTotal > max) max = crossTotal;

let revTotal = 0;
for(let idx = 0; idx < num; idx++){
  revTotal += board[idx][num - 1 - idx];
};

if(revTotal > max) max = revTotal;

console.log(max);
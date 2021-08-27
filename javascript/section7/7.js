"use strict";
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const num = Number(input[0]);
const list = [];
for(let idx = 1; idx <= num; idx++){
  const [x,y] = input[idx].split(' ').map(x => Number(x));
  list.push([x,y]);
}
list.sort((a,b) => {
  if(a[0] === b[0]) return a[1] - b[1];
  return a[0] - b[0];
})

console.log(list.map(x => x.join(' ')).join('\n'));
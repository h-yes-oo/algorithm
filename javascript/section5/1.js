const fs = require("fs");
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const n = parseInt(input[0]);
const first = input[1].split(' ').map(x => parseInt(x));
const m = parseInt(input[2]);
const second = input[3].split(' ').map(x => parseInt(x));

let i = 0;
let j = 0;
let result = [];
while(i < n && j < m){
  if(first[i] < second[j]) {
    result.push(first[i++]);
  } else {
    result.push(second[j++]);
  }
}

while(j < m) result.push(second[j++]);
while(i < n) result.push(first[i++]);

console.log(result.join(' '));
const fs = require("fs");
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const n = parseInt(input[0]);
const first = input[1].split(' ').map(x => parseInt(x));
const m = parseInt(input[2]);
const second = input[3].split(' ').map(x => parseInt(x));

first.sort((a,b) => a-b);
second.sort((a,b) => a-b);

result = [];

let i = 0;
let j = 0;

while(i < n && j < m){
  if(first[i] === second[j]) {
    result.push(first[i]);
    i++; j++;
  }
  else if(first[i] < second[j]) i++;
  else j++;
}

console.log(result.join(' '));

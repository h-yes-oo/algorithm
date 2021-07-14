const fs = require("fs");
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const num = parseInt(input[0]);
const elem = input[1].split(' ').map(x => parseInt(x));


const result = elem.filter((val, idx, arr) => {
  return idx == 0 || val > arr[idx-1]});


const sol = [];
sol.push(elem[0]);
for(let idx = 1; idx < num; idx++){
  if(elem[idx] > elem[idx-1]) sol.push(elem[idx]);
}

const print1 = `${result.join(" ")}\n`
const print2 = `${sol.join(" ")}\n`
console.log(print1,print2);
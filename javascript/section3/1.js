const fs = require("fs");
const input = fs.readFileSync('/dev/stdin').toString().split('\n')[0];

let flag = true;
let len = input.length;
let lowInput = input.toLowerCase();
for(let idx = 0; idx < Math.floor(len/2); idx++){
  if(lowInput[idx] !== lowInput[len-1-idx]){
    flag = false;
    break;
  }
}

if(flag) console.log("YES");
else console.log("NO");
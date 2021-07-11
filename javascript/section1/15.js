const fs = require("fs");
const input = fs.readFileSync('/dev/stdin').toString().split('\n')[0];

const len = input.length;
const mid = Math.floor(len / 2)

if(len % 2 == 0) console.log(input.substring(mid-1, mid+1));
else console.log(input[mid]);
const fs = require("fs");
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const num = parseInt(input[0]);

let result = input[1].length;
let sol = 1;
for(let i = 2; i < num; i++){
  if(input[i].length > result){
    result = input[i].length;
    sol = i;
  }
}

console.log(input[sol]);
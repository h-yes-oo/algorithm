// 앞 사람보다 키가 큰 사람의 수
"use strict"
const fs = require("fs");
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const num = parseInt(input[0]);
const students = input[1].split(' ').map(x => parseInt(x));

// let result = [];
// result.push(students[0]);
let count = 1;
let max = students[0];
for(let idx = 0; idx < num; idx++){
  if(students[idx] > max){
    //result.push(students[idx]);
    count += 1;
    max = students[idx];
  }
}

console.log(count);
const fs = require("fs");
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const first = input[0].toString().split(' ');
const second = input[1].toString().split(' ');

const day = Number(first[0]);
const cars = second.map(x => Number(x));

function solution(day, cars){
  let sol = 0;
  for(let car of cars){
    if(car % 10 === day ){
      sol += 1;
    }
  }
  return sol;
}

console.log(solution(day, cars));
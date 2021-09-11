"use strict";
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const [num, limit] = input[0].split(' ').map(x => Number(x));
let list = [];
for(let i = 1; i <= num; i++){
  const [score, time] = input[i].split(' ').map(x => Number(x));
  list.push([score, time]);
}

const sol = (num, list, limit) => {
  // memo[i] = i시간 까지 얻을 수 있는 최대 점수
  let memo = Array.from({length: limit+1}, () => 0);
  for(let x of list){
    const time = x[1];
    const score = x[0];
    for(let idx = limit; idx >= time; idx-- ){
      memo[idx] = Math.max(memo[idx], memo[idx - time] + score);
    }
  }
  console.log(memo[limit]);
};

sol(num, list, limit);
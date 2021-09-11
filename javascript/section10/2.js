"use strict";
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const num = Number(input[0]);

const sol = (num) => {
  // n까지 가는 방법의 수 = n-1까지 가는 방법의 수 + n-2까지 가는 방법의 수
  let memo = Array.from({length : num+2}, () => 0);
  memo[1] = 1;
  memo[2] = 2;
  for(let idx = 3; idx <= num + 1; idx++){
    if(memo[idx] !== 0) continue;
    else{
      memo[idx] = memo[idx-1] + memo[idx-2];
    }
  }
  console.log(memo[num+1]);
}

sol(num);

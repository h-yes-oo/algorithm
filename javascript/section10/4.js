"use strict";
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const num = Number(input[0]);
const coins = input[1].split(' ').map(x => Number(x));
const money = Number(input[2]);

const sol = (num, coins, money) => {
  // memo[i] = i원을 거슬러 주는데에 필요한 최소 동전 개수
  let memo = Array.from({length: money + 1}, () => Number.MAX_SAFE_INTEGER);
  // memo[i + coins[j]] = memo[i] + 1;
  // memo[i] = memo[i - + coins[j]] + 1;
  memo[0] = 0;
  for(let idx = 0; idx < num; idx++){
    for(let j = coins[idx]; j <= money; j++){
      memo[j] = Math.min(memo[j], memo[j-coins[idx]] + 1)
    }
  }
  console.log(memo);
  console.log(memo[money]);
};

sol(num, coins, money);

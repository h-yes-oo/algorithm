"use strict";
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const [n, k] = input[0].split(' ').map(x => Number(x));
const list = input[1].split(' ').map(x => Number(x));
const m = Number(input[2]);

const sol = (n, k, list, m) => {
  let answer = 0;
  // n개 중 k를 뽑는 조합 구하기
  const DFS = (level, start, sum) => {
    if(level === k){
      // m의 배수인지 확인
      if(sum % m === 0) answer++;
    } else {
      for(let idx = start; idx < n; idx++){
        DFS(level + 1, idx + 1, sum + list[idx]);
      }
    }
  };
  DFS(0,0,0);
  console.log(answer);
};

sol(n,k,list,m);
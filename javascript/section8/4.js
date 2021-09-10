"use strict";
// get input
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const num = Number(input[0]);

const sol = (num) => {
  let answer = [];
  let check = Array.from({length: num + 1}, (v,k) => 0);
  const DFS = (level) => {
    if(level === num+1) {
      // 끝났을 때
      let ans = [];
      for(let i = 1; i <= num; i++){
        if(check[i] === 1) ans.push(i);
      }
      if(ans.length > 0) answer.push(ans.join(' '));
      return;
    }
    // 이 level을 포함하고 넘어가기
    check[level] = 1;
    DFS(level+1);
    // 이 level을 포함하지 않고 넘어가기
    check[level] = 0;
    DFS(level+1);
  }
  DFS(1);
  console.log(answer.join('\n'));
};

sol(num);
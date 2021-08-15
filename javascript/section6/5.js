// 레이저가 닫힐 때 : 현재 열린 괄호 수만큼 왼쪽 파편 생김

// 레이저가 아닌 쇠막대기가 닫힐 때 : 한개의 오른쪽 파편이 생김

"use strict"
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const inp = input[0];

const sol = (inp) => {
  let stack = 0;
  let left = false;
  let answer = 0;
  for(let x of inp){
    if(x === '('){
      stack++;
      left = true;
    } else if (x===')') {
      stack--;
      if(left){
        answer += stack;
      } else answer += 1;
      left = false;
    }
  }
  console.log(answer);
}

sol(inp);
solution(inp);
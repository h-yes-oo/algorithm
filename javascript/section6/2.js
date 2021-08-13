const fs = require("fs");
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const inp = input[0];

const sol = (inp) => {
  let par = 0;
  let answer = '';
  for(let x of inp){
    if(x === '(') par++;
    else if(x === ')') par--;
    else {
      if(par === 0) answer += x;
    }
  }
  console.log(answer);
}

const usingStack = (inp) => {
  let stack = [];
  for(let x of inp){
    if(x === ')') {
      while(stack.pop() !== '(');
    }
    else stack.push(x);
  }
  console.log(stack.join(''))
}

sol(inp);
usingStack(inp);
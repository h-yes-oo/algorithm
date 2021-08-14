const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const inp = input[0];

const sol = (inp) => {
  const stack = [];
  for(let x of inp){
    if(x === '+'){
      let second = stack.pop();
      let first = stack.pop();
      stack.push(first + second);
    } else if (x === '-'){
      let second = stack.pop();
      let first = stack.pop();
      stack.push(first - second);
    } else if (x === '*'){
      let second = stack.pop();
      let first = stack.pop();
      stack.push(first * second);
    } else if (x === '/'){
      let second = stack.pop();
      let first = stack.pop();
      stack.push(first / second);
    } else {
      stack.push(parseInt(x));
    }
  }
  console.log(stack[0]);
};

sol(inp);

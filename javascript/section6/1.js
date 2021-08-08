const fs = require("fs");
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const inp = input[0];

const sol = (inp) => {
  let ans = 0;
  for(let x of inp){
    if(x==='(') ans++;
    else if(x===')') ans--;
    if(ans < 0) return 'NO';
  }
  if(ans === 0) return 'YES';
  else return 'NO';
}

const usingPushPop = (inp) => {
  let ans = []
  for(let x of inp){
    if(x==='(') ans.push(x);
    else if(x===')') {
      if(ans.length === 0) return 'NO';
      ans.pop();
    }
  }
  if(ans.length === 0) return 'YES';
  else return 'NO';
}

console.log(sol(inp));
console.log(usingPushPop(inp));
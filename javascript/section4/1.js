const fs = require("fs");
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const num = parseInt(input[0]);
const list = input[1].split(' ').map(x => parseInt(x));

let max = Number.MIN_SAFE_INTEGER;
let result = -1;

function getTotal(num){
  let total = 0;
  while(Math.floor(num / 10) > 0){
    total += num % 10;
    //num = num을 10으로 나눈 몫
    num = Math.floor(num / 10);
  }
  total += num;
  return total;
}

list.forEach((val, idx) => {
  if(max < getTotal(val) || (max == getTotal(val) && val > result)) {
    max = getTotal(val);
    result = val;
  }
});

console.log(result);
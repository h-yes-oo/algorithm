const fs = require("fs");
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const [first, second] = input;

const inspectMap = (map) => {
  for(let key in map){
    if(map[key] !== 0) return false;
  }
  return true;
}

const sol = (first, second) => {
  let answer = 0;
  const map = {};
  for(let x of second){
    if(map[x] === undefined) map[x] = 1;
    else map[x] += 1;
  }
  let end = second.length;
  for(let idx = 0; idx < end; idx++){
    let letter = first.charAt(idx);
    if(map[letter] === undefined) map[letter] = -1;
    else map[letter] -= 1;
  }
  if(inspectMap(map)) answer++;
  let len = first.length;
  let start = 0;
  for(; end < len; end++){
    let flag = true;
    let left = first.charAt(start);
    let right = first.charAt(end);
    map[left] += 1;
    if(map[right] === undefined) {
      map[right] = -1;
      flag = false;
    }
    else map[right] -= 1;
    if(flag)
      if(inspectMap(map)) answer++;
    start++;
  }
  console.log(answer);
};

sol(first, second);
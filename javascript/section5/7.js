const fs = require("fs");
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const [first, second] = input;

const sol = (first, second) => {
  let map = {};
  for(let x of first){
    if(map[x] === undefined) map[x] = 1;
    else map[x] += 1;
  }
  for(let y of second){
    if(map[y] === undefined) return 'NO';
    else map[y] -= 1;
  }
  for(let key in map){
    if(map[key] !== 0) return 'NO';
  }
  return 'YES';
}

const usingMap = (first, second) => {
  let map = new Map();
  for(let x of first){
    if(!map.has(x)) map.set(x, 1);
    else map.set(x, map.get(x)+1);
  }
  for(let y of second){
    if(!map.has(y)) return 'NO';
    else map.set(y, map.get(y)-1);
  }
  for(let [key, value] of map){
    if(value !== 0) return 'NO';
  }
  return ('YES');
}

console.log(sol(first, second));
console.log(usingMap(first, second));
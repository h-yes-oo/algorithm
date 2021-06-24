const fs = require("fs");
const input = fs.readFileSync('/dev/stdin').toString().split(' ');
const num = input.map(x => parseInt(x));

const odd = num.filter(x => x%2 == 0 ? false : true);

let min = odd[0];
let sum = 0;
for(let i = 0; i < odd.length; i++){
  if(odd[i] < min) min = odd[i];
  sum += odd[i];
}

console.log(sum);
console.log(min);
console.log(Math.min(...odd));
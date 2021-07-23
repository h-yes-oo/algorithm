const fs = require("fs");
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const [num, order] = input[0].split(' ').map(x => parseInt(x));
const cards = input[1].split(' ').map(x => parseInt(x));

let result = new Set();
for(let first = 0; first < num; first++){
  for(let second = first + 1; second < num; second++){
    for(let third = second + 1; third < num; third++){
      result.add(cards[first]+cards[second]+cards[third]);
    }
  }
}

result = Array.from(result);
result.sort((a,b) => b-a);
console.log(result[order-1]);
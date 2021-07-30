const fs = require("fs");
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const [n,m] = input[0].split(' ').map(x => parseInt(x));
const list = input[1].split(' ').map(x => parseInt(x));


function sol1(n,m,list){
  let answer = 0;
  for(let start = 0; start < n; start++){
    let end = start;
    let sum = list[end++];
    while(sum <= m){
      answer++;
      sum += list[end++];
    }
  }
  console.log(answer);
}

sol1(n,m,list);

function sol2(n,m,list){
  let answer = 0;
  let start = 0;
  let sum = 0;
  for(let end = 0; end < n; end++){
    sum += list[end];
    while(sum > 5){
      sum -= list[start++];
    }
    answer += end - start + 1;
  }
  console.log(answer);
}

sol2(n,m,list);
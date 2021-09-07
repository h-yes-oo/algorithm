"use strict";
// get input
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const num = Number(input[0]);
const list = [];
for(let idx = 1; idx <= num; idx++){
  const [x,y] = input[idx].split(' ').map(x => Number(x));
  list.push([x,y]);
}

// 시간 순서대로 정렬 후 이벤트 발생
const sol = (num, list) => {
  const startDate = new Date();
  const coming = list.slice().sort((a,b)=>{
    if(a[0] === b[0]) return a[1] - b[1];
    return a[0] - b[0];
  });

  const going = list.slice().sort((a,b)=>{
    if(a[1] === b[1]) return a[0] - b[0];
    return a[1] - b[1];
  });

  let ans = -1;
  let now = 0;
  let cidx = 0;
  let gidx = 0;
  // 사람이 오는 이벤트가 사람이 가는 이벤트 보다는 먼저 표현될 것이기 때문에 
  while(cidx < num){
    // 가장 최근 이벤트가 사람이 오는 것인 경우
    if(coming[cidx][0] < going[gidx][1]){
      cidx++;
      now++;
    } else if (coming[cidx][0] > going[gidx][1]) {
      // 가장 최근 이벤트가 사람이 가는 것인 경우
      gidx++;
      now--;
    } else {
      // 동시에 오고 가는 경우
      cidx++;
      gidx++;
    }
    ans = Math.max(ans, now)
  }
  console.log(ans);
  console.log('first running(s)@',(new Date().getTime() - startDate.getTime()) / 1000);
}

function solution(times){
  const startDate = new Date();
  let answer=Number.MIN_SAFE_INTEGER;
  let T_line=[];
  for(let x of times){
      T_line.push([x[0], 's']);
      T_line.push([x[1], 'e']);
  }
  T_line.sort((a, b)=>{
      if(a[0]===b[0]) return a[1].charCodeAt()-b[1].charCodeAt();
      else return a[0]-b[0];
  });
  let cnt=0;
  for(let x of T_line){
      if(x[1]==='s') cnt++;
      else cnt--;
      answer=Math.max(answer, cnt);
  }
  console.log(answer);
  console.log('second running(s)@',(new Date().getTime() - startDate.getTime()) / 1000);
}

sol(num, list);
solution(list);

/*
70
14 18
12 15
15 20 
20 30 
5 14
14 18
12 15
15 20 
20 30 
5 14
14 18
12 15
15 20 
20 30 
5 14
14 18
12 15
15 20 
20 30 
5 14
14 18
12 15
15 20 
20 30 
5 14
14 18
12 15
15 20 
20 30 
5 14
14 18
12 15
15 20 
20 30 
5 14
14 18
12 15
15 20 
20 30 
5 14
14 18
12 15
15 20 
20 30 
5 14
14 18
12 15
15 20 
20 30 
5 14
14 18
12 15
15 20 
20 30 
5 14
14 18
12 15
15 20 
20 30 
5 14
14 18
12 15
15 20 
20 30 
5 14
14 18
12 15
15 20 
20 30 
5 14
*/
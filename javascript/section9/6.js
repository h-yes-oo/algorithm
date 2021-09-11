"use strict";
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const [hs, cow] = input[0].split(' ').map(x => Number(x));

const sol = (hs, cow) => {
  let Q = [hs];
  let trial = 0;
  while(Q.length){
    const now = Q.slice();
    for(let x of now){
      Q.shift();
      if(x === cow){
        console.log(trial);
        return;
      } else {
        Q.push(x + 1);
        Q.push(x - 1);
        Q.push(x + 5);
      }
    }
    trial++;
  }
};

sol(hs, cow);

function solution(hs, cow){  
  let answer=0;
  let check=Array.from({length:10001}, ()=>0);
  let dist=Array.from({length:10001}, ()=>0);
  let queue=[];
  // 초기화
  queue.push(hs);
  check[hs]=1;
  dist[hs]=0;
  // BFS
  while(queue.length){
      let x=queue.shift();
      for(let nx of [x-1, x+1, x+5]){
          if(nx===cow) return dist[x]+1;
          if(nx>0 && nx<=10000 && check[nx]===0){
              check[nx]=1;
              queue.push(nx);
              dist[nx]=dist[x]+1;
          }
      }
  }
  return answer;
}

console.log(solution(hs, cow));

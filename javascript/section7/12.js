"use strict";
// get input
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const [n , m] = input[0].split(' ').map(x => Number(x));
const list = input[1].split(' ').map(x => Number(x));

// 정렬
// 1 2 4 8 9
// 거리의 최소값 lt : 1
// 거리의 최대값 rt : (끝점 - 시작점) / (말의 수 - 1)
// 넣을 수 있는 최대 거리 찾기
// 넣을 수 있다면 lt = mid + 1
// 넣을 수 없다면 rt = mid - 1

const can = (horse, pos, limit) => {
  let count = 1;
  let next = pos[0] + limit;
  for(let x of pos){
    if(x >= next){
      count++;
      next = x + limit;
    }
    if(count === horse) return true;
  }
  if(count < horse) return false;
}

const sol = (num, horse, list) => {
  const pos = list.slice();
  pos.sort((a,b) => a-b);
  let lt = 1; 
  let rt = parseInt((pos[num-1] - pos[0]) / (horse - 1));
  let answer = 1;
  while(lt <= rt){
    let mid = parseInt((lt+rt)/2);
    if(can(horse, pos, mid)) {
      lt = mid + 1;
      answer = mid;
    }
    else rt = mid - 1;
  }
  console.log(answer);
  return;
}

sol(n, m, list);

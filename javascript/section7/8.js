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

// 끝나는 시간이 빠른 순서대로 정렬 후 for 문 돌리기
const sol = (num, list) => {
  let arr = list.slice();
  arr.sort((a,b) => {
    if(a[1] === b[1]) return a[0]-b[0]
    return a[1]-b[1]
  });
  let count = 0;
  let end = 0;
  for(let i = 0; i < num; i++){
    if(arr[i][0] >= end){
      count++;
      end = arr[i][1];
    }
  }
  console.log(count);
}

sol(num, list);

/*
5
1 4
2 3
3 5
4 6
5 7
*/

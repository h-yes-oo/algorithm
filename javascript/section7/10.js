"use strict";
// get input
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const [n , m] = input[0].split(' ').map(x => Number(x));
const list = input[1].split(' ').map(x => Number(x));

const sol = (n , m , list) => {
  const sorted = list.slice().sort((a,b) => a - b);
  let start = 0;
  let end = n-1;
  let mid;
  while(start <= end){
    mid = parseInt((end + start)/2);
    let now = sorted[mid];
    // 찾는 값이 더 작으면
    if(now > m) end = mid-1;
    // 찾는 값이 더 크면
    else if(now < m) start = mid+1;
    else break;
  }
  console.log(mid+1);
  return;
}

sol(n, m, list);
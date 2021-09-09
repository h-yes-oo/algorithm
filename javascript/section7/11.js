"use strict";
// get input
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const [n , m] = input[0].split(' ').map(x => Number(x));
const list = input[1].split(' ').map(x => Number(x));

// 최소 : sum(list) / 3 보다는 커야 함
const count = (songs, limit) => {
  let ans = 1;
  let bucket = 0;
  for(let x of songs){
    if(bucket + x <= limit){
      bucket += x;
    } else {
      ans++;
      bucket = x;
    }
  }
  return ans;
}

const sol = (n, m, list) => {
  const arr = list.slice();
  let limit = parseInt(arr.reduce((a,b)=> a+b, 0) / 3);
  while(true){
    const ans = count(arr, limit);
    if(ans > m) limit++;
    else break;
  }
  console.log(limit);
  return;
}

function solution(m, list){
  let songs = list.slice();
  // 최소 곡 한 개는 담을 수 있어야 한다
  let lt = Math.max(...songs);
  // 최대로는 모든 곡을 한 테이프에 담는다
  let rt = songs.reduce((a,b) => a+b, 0);
  let answer;
  while(lt <= rt){
    let limit = parseInt((lt+rt)/2);
    let ans = count(songs, limit);
    // 원하는 것보다 많은 DVD가 필요하면 limit가 더 커져야 함
    if(ans > m) lt = limit + 1;
    // 원하는 것보다 적은 DVD가 필요하면 limit이 최대한 낮아질 때까지 시행
    // 답을 설정하고, 더 작은 범위에서 답이 나올 수 있는지 해보기
    else {
      answer = limit;
      rt = limit - 1;
    }
  }
  console.log(answer);
  return;
}

sol(n, m, list);
solution(m, list);

/*
9 3
1 2 3 4 5 6 7 8 9
*/
"use strict";
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const [n, f] = input[0].split(' ').map(x => Number(x));

// 최종 level은 n과 같음
// 한 줄에 하나만 정해지면 나머지는 다 정해짐
// 가망이 없으면 자를 것
// 가망이 없다는 것은 최종 level이 아닌데 1보다 작은 값이 나올 때

const sol = (n,f) => {
  const DFS = (level, list) => {
    if(level === n-1){
      for(let i = 1; i < list[0]; i++){
        let arr = [];
        arr.push(i);
        let flag = true;
        for(let idx = 0; idx < level; idx++){
          let next = list[idx] - arr[idx];
          if(next < 1) {
            flag = false;
            continue;
          }
          else arr.push(next);
        }
        if(flag) console.log(arr.join(' '));
      }
    } else {
      for(let i = 2; i < list[0]; i++){
        let arr = [];
        arr.push(i);
        for(let idx = 0; idx < level; idx++){
          let next = list[idx] - arr[idx];
          if(next < 2) return;
          else arr.push(next);
        }
        DFS(level + 1, arr);
      }
    }
  };
  DFS(1,[f]);
}

// sol(n,f);

const can = (list, f, last) => {
  let arr = list.slice();
  for(let fidx = 0; fidx < last; fidx++){
    for(let bidx = last; bidx > fidx; bidx--){
      arr[bidx] += arr[bidx-1];
    }
  }
  if(arr[arr.length-1] === f) return true;
  else return false;
}

const solution = (n,f) => {
  let check = Array.from({length: n}, () => 0);
  let tmp = Array.from({length: n}, () => 0);
  let flag = false;
  const DFS = (level) => {
    if(flag) return;
    if(level === n) {
      // 수열 완성 되면 체크 하기
      if(can(tmp, f, n-1)) {
        console.log(tmp.join(' '));
        flag = true;
        return;
      };
    } else {
      for(let i = 0; i < n; i++){
        if(check[i] === 0){
          check[i] = 1;
          tmp[level] = i + 1;
          DFS(level + 1);
          check[i] = 0;
        }
      }
    }
  };
  DFS(0);
}

solution(n,f);
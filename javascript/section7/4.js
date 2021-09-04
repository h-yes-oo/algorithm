"use strict";
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const num = Number(input[0]);
const list = input[1].split(' ').map(x => Number(x));

console.log(list);

const insertionSort = (num, list) => {
  let ans = list.slice();
  //i - 1까지는 정렬 되어 있고, ans[i]의 자리를 찾기
  for(let i = 0; i < num; i++){
    // 자리를 찾아야 하는 애가 tmp
    let tmp = ans[i];
    let j;
    for(j = i - 1; j >= 0; j-- ){
      // tmp 보다 크면 뒤로 하나씩 미룬다
      if(ans[j] > tmp) ans[j+1] = ans[j];
      // tmp 보다 작으면 거기가 tmp의 자리 !!
      else break;
    }
    ans[j+1] = tmp;
  }
}

insertionSort(num, list);
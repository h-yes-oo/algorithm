"use strict";
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const n = Number(input[0]);
const inp = input[1].split(' ').map(x => Number(x));

const selectionSort = (n, inp) => {
  for(let idx = 0; idx < n; idx++){
    //array[idx] 에 뒤의 숫자 중 가장 작은 수를 넣는다
    let small = idx;
    for(let j = idx + 1; j < n; j++){
      if(inp[j] < inp[small]) small = j;
    }
    [inp[idx], inp[small]] = [inp[small], inp[idx]]
  }
  console.log(inp.join(' '));
}

selectionSort(n, inp);
"use strict";
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const num = Number(input[0]);
const list = input[1].split(' ').map(x => Number(x));

// 가장 뒷 자리에 가장 큰 수가 정해짐
const bubbleSort = (num, list) => {
  let answer = list.slice();
  for(let i = 0; i < num - 1; i++){
    for(let j = 0; j < num - i - 1; j++){
      if(answer[j] > answer[j+1]) {
        [ answer[j], answer[j+1] ] = [ answer[j+1], answer[j] ]
      }
    }
  }
  console.log(answer.join(' '));
}

bubbleSort(num, list);


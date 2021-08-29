"use strict";
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const num = Number(input[0]);
const list = input[1].split(' ').map(x => Number(x));

const usePush = (num, list) => {
  let negative = [];
  let positive = [];
  for(let i = 0; i < num; i++){
    const x = list[i];
    if(x < 0) negative.push(x);
    else positive.push(x);
  }
  console.log(negative.join(' ') + ' ' + positive.join(' '));
}

const useSort = (num, list) => {
  let answer = list.slice();
  for(let i = 0; i < num - 1; i++){
    for(let j = 0; j < num - i -1; j++){
      if(answer[j] > 0 && answer[j+1] < 0){
        [answer[j], answer[j+1]] = [answer[j+1], answer[j]];
      }
    }
  }
  console.log(answer.join(' '));
}

usePush(num, list);
useSort(num, list);


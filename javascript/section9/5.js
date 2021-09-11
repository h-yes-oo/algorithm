"use strict";

const sol = () => {
  let Q = [1];
  let answer = '';
  while(Q.length){
    let x = Q.shift();
    answer += `${x} `;
    for(let next of [2*x, 2*x+1]){
      if(next < 8) {
        Q.push(next);
      }
    }
  }
  console.log(answer);
};

sol();
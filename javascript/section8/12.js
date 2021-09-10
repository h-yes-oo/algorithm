"use strict";
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const [n, r] = input[0].split(' ').map(x => Number(x));

const sol = (n,r) => {
  let board = Array.from(
    {length: n+1}, 
    () => Array.from(
      {length: r+1}, 
      () => 0
      )
    );
  const DFS = (n,r) => {
    if (n === r || r === 0) return 1;
    else {
      if(board[n][r] !== 0) return board[n][r];
      else return board[n][r] = DFS(n-1, r-1) + DFS(n-1, r);
    }
  }
  const ans = DFS(n,r);
  console.log(ans);
}

sol(n,r);
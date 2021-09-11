"use strict";
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const [n, m] = input[0].split(' ').map(x => Number(x));
let graph = Array.from(
  {length: n+1},
  ()=>Array(n+1).fill(0)
);
for(let i = 1; i < m + 1; i++){
  const [x, y] = input[i].split(' ').map(x => Number(x));
  graph[x][y] = 1;
}

const sol = (n,m, board) => {
  let answer = 0;
  let check = Array.from({length: n+1}, () => 0);
  let path = [];
  const DFS = (vertex) => {
    if(vertex === n){
      answer++;
      // console.log(path.join(' '));
    } else {
      for(let idx = 1; idx <=n; idx++){
        if(board[vertex][idx] === 1 && check[idx] === 0){
          path.push(idx);
          check[idx] = 1;
          DFS(idx);
          path.pop();
          check[idx] = 0;
        }
      }
    }
  }
  check[1] = 1;
  path.push(1);
  DFS(1);
  console.log(answer);
};

sol(n,m,graph);

/*
5 9 
1 2 
1 3 
1 4 
2 1 
2 3 
2 5 
3 4 
4 2 
4 5
*/
"use strict";
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const [n, m] = input[0].split(' ').map(x => Number(x));
let graph = Array.from(
  {length: n+1},
  ()=>[]
);
for(let i = 1; i < m + 1; i++){
  const [x, y] = input[i].split(' ').map(x => Number(x));
  graph[x].push(y);
}

const sol = (n,m,graph) => {
  let check = Array.from({length: n+1}, () => 0);
  let path = [];
  let answer = 0;
  const DFS = (vertex) => {
    if(vertex === n){
      // console.log(path.join(' '));
      answer++;
    } else{
      for(let x of graph[vertex]){
        if(check[x] === 0){
          check[x] = 1;
          path.push(x);
          DFS(x);
          check[x] = 0;
          path.pop();
        }
      }
    }
  }
  path.push(1);
  check[1] = 1;
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
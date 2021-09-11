"use strict";
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
let graph = [];
for(let i = 0; i < 7; i++){
  graph.push(input[i].split('').map(x => Number(x)));
}

const sol = (graph) => {
  // 상 하 좌 우
  const dr = [-1, 1, 0, 0];
  const dc = [0, 0, -1, 1];
  let answer = 0;
  const DFS = (r,c) => {
    if(r === 6 && c === 6){
      answer++;
    } else {
      for(let idx = 0; idx < 4; idx++){
        const nr = r + dr[idx];
        const nc = c + dc[idx];
        if(0 <= nr && nr < 7 && 0 <= nc && nc < 7 && graph[nr][nc] === 0){
          graph[nr][nc] = 1;
          DFS(nr,nc);
          graph[nr][nc] = 0;
        }
      }
    }
  }
  graph[0][0] = 1;
  DFS(0,0);
  console.log(answer);
}

sol(graph);

/*
0000000
0111110
0001000
1101011
1100001
1101100
1000000
*/
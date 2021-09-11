"use strict";
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const n = Number(input[0]);
let graph = [];
for(let i = 1; i < n+1; i++){
  graph.push(input[i].split('').map(x => Number(x)));
}

const sol = (n, graph) => {
  let answer = 0;
  // 상하좌우 대각선까지
  const dr = [1, -1, 0, 0, -1, -1, 1, 1];
  const dc = [0, 0, -1, 1, 1, -1, 1, -1];
  for(let r = 0; r < n; r++){
    for(let c = 0; c < n; c++){
      if(graph[r][c] === 1){
        answer++;
        let queue = [[r,c]];
        while(queue.length){
          const [x,y] = queue.shift();
          graph[x][y] = 0;
          for(let idx = 0; idx < 8; idx++){
            const nx = x + dr[idx];
            const ny = y + dc[idx];
            if(0 <= nx && nx < n && 0<= ny && ny < n && graph[nx][ny] === 1){
              queue.push([nx, ny]);
            }
          }
        }
      }
    }
  }
  console.log(answer);
}

sol(n,graph);

/*
7
1100010
0110110
0100000
0001011
1101100
1000100
1010100
*/
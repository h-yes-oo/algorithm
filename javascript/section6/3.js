const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
const moves = [1,5,3,5,1,2,1,4];

// n 만큼의 빈 array를 갖는 2차원 array col 초기화
const n = board.length;
let stacks = Array.from({length: n}, () => []);
let accumulate = [];

// board의 뒤에서 부터 0을 만나지 않을 때까지 push
for(let col = 0; col < n; col++){
  let row = n-1;
  for(let x; x = board[row][col] && x !== 0 && row >= 0; row --){
    stacks[col].push(board[row][col]);
  }
}

// moves 의 원소 x마다 x-1 인덱스의 col에서 pop
let answer = 0;

for(let x of moves){
  let idx = x-1;
  let doll = stacks[idx].pop();
  if(doll !== undefined){
    if(doll === accumulate[accumulate.length - 1]) {
      accumulate.pop();
      answer += 2;
      // answer++;
      // let x;
      // for(; x = accumulate.pop() && doll === x;) {
      //   answer++;
      // }
      // accumulate.push(x);
    }
    else accumulate.push(doll);
  }
};

console.log(answer);
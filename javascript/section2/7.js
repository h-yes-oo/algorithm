const fs = require("fs");
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const num = parseInt(input[0]);
const inp = input.splice(1,num);
const board = [];
inp.forEach((val, idx) => board.push(
  val.split(' ').map(x => parseInt(x)
)));

let dx=[-1, 0, 1, 0];
let dy=[0, 1, 0, -1];

let answer = 0;

for(let row = 0; row < num; row++){
  for(let col = 0; col < num; col++){
    let flag = true;
    for(let trial = 0; trial < 4; trial++){
      let nx = row + dx[trial];
      let ny = col + dy[trial];
      if(nx >= 0 && nx < num
         && ny >=0 && ny < num
         && board[nx][ny] >= board[row][col]
        ) {
          flag = false;
          break;
        }
    }
    if(flag) answer++;
  }
}

console.log(answer);
const fs = require("fs");
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const [n , m] = input[0].split(' ').map(x => parseInt(x));
let board = [];
for(let i = 1; i <= m; i++){
  let list = input[i].split(' ').map(x => parseInt(x)).splice(0,n);
  board.push(list);
}

// (first, second)의 조합이 m번 있는 경우 답으로 출력
// 1...n 까지
let answer = 0;
for(let first = 1; first <= n; first++){
  for(let second = 1; second <= n; second++){
    //board의 각 row에 대하여 등수 검사
    let count = 0;
    for(let test = 0; test < m; test++){
      let firstRank = -1;
      let secondRank = -1;
      // first와 second의 등수 찾기
      for(let idx = 0; idx < n; idx++){
        if(board[test][idx] === first) firstRank = idx;
        if(board[test][idx] === second) secondRank = idx;
      }
      //first보다 second의 등수가 크면 count 추가
      if(firstRank < secondRank) count++;
    }
    if(count === m) answer++;
  }
}

console.log(answer);
const fs = require("fs");
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const [num, budget] = input[0].split(' ').map(x => parseInt(x));

const info = [];
for(let idx = 1; idx < num + 1; idx++){
  info.push(input[idx].split(' ').map(x => parseInt(x)));
}

// 총 가격 순 정렬하되, 할인된 가격도 같은 인덱스로 배열 가져야 함
// (a[0] + a[1]) < (b[0] + b[1])
info.sort((a, b) => (a[0] + a[1]) - (b[0] + b[1]));

// 기준이 없기 때문에 모든 경우를 다 해본다
// 각각을 할인 했을 때, 정렬된 순서로 다 더하기
let answer = -1;
for(let sale = 0; sale < num; sale++){
  // 할인된 상품
  let price = info[sale][0] / 2 + info[sale][1];
  if(price > budget) continue;
  let count = 1;
  for(let idx = 0; idx < num; idx++){
    // 이미 할인된 상품 제외
    if(sale === idx) continue;
    // 이번 상품을 더했을 때의 가격
    const newPrice = price + info[idx][0] + info[idx][1];
    // 가격이 초과되면 종료
    if(newPrice > budget) {
      break;
    }
    count++;
    price = newPrice;
  }
  // answer를 현재 count와 비교
  answer = Math.max(answer, count);
}

console.log(answer);


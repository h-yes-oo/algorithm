const fs = require("fs");
const input = fs.readFileSync('/dev/stdin').toString().split('\n')[0];

let count = 1;
let before = '';
let result = '';
for(let letter of input){
  //새로운 문자가 나타나면 해당 문자를 추가하고, 카운트가 1보다 크면 추가
  //카운트는 1로 초기화
  if(letter !== before){
    if(count !== 1) result += count;
    before = letter;
    result += letter;
    count = 1;
  } else {
    count++;
  }
}
//마지막 문자의 카운트
if(count !== 1) result += count;

console.log(result);
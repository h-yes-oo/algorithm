const fs = require("fs");
const input = fs.readFileSync('/dev/stdin').toString();

function sol(word){
  let result = '';
  // 마지막 개행 문자가 포함되기 때문에 length -1 을 해줬는데 흠
  for(let i = 0; i < word.length - 1; i++){
    if(word[i] === 'A') result += '#';
    else result += word[i];
  }
  return result;
}

function solution(word){
  let result = '';
  // 마지막 개행 문자가 포함되지 않도록
  for(let letter of word){
    if(letter === 'A') result += '#';
    else if(letter !== '\n') result += letter;
  }
  return result;
}

console.log(input.length);
console.log(solution(input));
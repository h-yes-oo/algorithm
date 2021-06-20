const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split(' ');
let a = parseInt(input[0]);
let b = parseInt(input[1]);
let c = parseInt(input[2]);

function solution(a,b,c){
  //find max
  let max;
  if(a>b) { max = a; }
  else { max = b; }
  if( c > max ) { max = c;}

  let sum = a + b + c;
  if((sum - max) <= max ) return("NO");
  else return("YES");
}

console.log(solution(a,b,c));
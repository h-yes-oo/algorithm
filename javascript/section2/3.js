const fs = require("fs");
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const num = parseInt(input[0]);
const A = input[1].split(' ').map(x => parseInt(x));
const B = input[2].split(' ').map(x => parseInt(x));

let print = '';
for(let idx = 0; idx < num; idx++){
  const a = A[idx]; const b = B[idx];
  if( a === b) print += 'D\n';
  else if ( a === 1 ) {
    if ( b == 2) print += 'B\n';
    else print += 'A\n';
  }
  else if ( a == 2 ) {
    if ( b == 3) print += 'B\n';
    else print += 'A\n';
  }
  else {
    if ( b == 1) print += 'B\n';
    else print += 'A\n';
  }
}

console.log(print.slice(0,-1));
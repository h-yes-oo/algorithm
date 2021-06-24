const fs = require("fs");
const input = fs.readFileSync('/dev/stdin').toString().split(' ');
const long = input[0];
const short = input[1].substr(0,1);

function sol1(s, t){
  let result = Array.from({length: s.length}, () => 0);

  for(let idx = 0; idx < s.length; idx++){
    if(s[idx] !== t){
      let count = 0;
      while(s[idx + count] !== t && s[idx - count] !== t){
        count++;
      }
      result[idx] = count;
    }
  }

  const print = result.join(' ');
  console.log(print);
}

//딱 두번만 탐색하면 되기 때문에 더 빠르고 간단한 해법
function sol2(s, t){
  let result = Array.from({length: s.length}, () => 0);
  let flag = 1000;
  for(let idx = 0; idx < s.length; idx++){
    const letter = s[idx];
    if(letter === t){
      flag = 0;
      result[idx] = flag;
    } else {
      flag++;
      result[idx] = flag;
    }
  }
  flag = 1000;
  for(let ridx = s.length - 1; ridx >= 0; ridx--){
    const letter = s[ridx];
    if(letter === t){
      flag = 0;
      // result[ridx] = flag;
    } else {
      flag++;
      result[ridx] = Math.min(flag, result[ridx]);
    }
  }
  const print = result.join(' ');
  console.log(print);
}

sol1(long,short);
sol2(long,short);
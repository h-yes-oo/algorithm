const fs = require("fs");
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const [n, vote] = input;

const useObject = (n,vote) => {
  const startDate = new Date();
  let result = {};

  for(let letter of vote){
    if(result[letter] === undefined) result[letter] = 1;
    else result[letter] += 1;
  }

  let sortable = [];

  for(let name in result) {
    sortable.push([name, result[name]]);
  };

  sortable.sort(function(a,b){
    return b[1] - a[1];
  });

  console.log(sortable[0][0]);
  console.log('useObject running(s)@',(new Date().getTime() - startDate.getTime()) / 1000);
};

const useMap = (n,vote) => {
  const startDate = new Date();
  let map = new Map();

  for(let letter of vote){
    if(map.has(letter)) map.set(letter, map.get(letter) + 1);
    else map.set(letter, 1);
  }

  let sortable = [];

  for(let [name, value] of map) {
    sortable.push([name, value]);
  };

  sortable.sort(function(a,b){
    return b[1] - a[1];
  });

  console.log(sortable[0][0]);
  console.log('useMap running(s)@',(new Date().getTime() - startDate.getTime()) / 1000);
};

useMap(n, vote);
useObject(n, vote);
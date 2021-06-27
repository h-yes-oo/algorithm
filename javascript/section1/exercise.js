a = [10,11,12,13,14];

a.forEach((elem,idx) => {
  console.log(elem, idx);
});

//map : 원본과 같은 길이의 새로운 배열 리턴
let answer = a.map((elem, i) => {
  return `${i}th element is ${elem}`;
})

//filter : 원본에서 주어진 조건을 만족하는 원소만 포함하는 새로운 배열을 리턴
let filtered = a.filter((elem, idx) => {
  return idx%2 == 0 && elem > 10;
})

//reduce : 두번째 인자에 배열의 원소들을 누적하여 callback ftn 적용
b = [1,3,5,7]

let reduced = b.reduce(function(acc, value){
  return acc * value;
}, 1);

function reduce(predicate, val){
  let result = val;
  for(let i = 0; i < a.length; i++){
    result = predicate(result, a[i])
  }
  return result;
}

console.log(answer);
console.log(filtered);
console.log(reduced);
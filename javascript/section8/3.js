const pre = () => {
  let ans = [];
  // 왼쪽 자식 : 본인 * 2 
  // 오른쪽 자식 : 본인 * 2 + 1
  const DFS = (num) => {
    if(num > 7) return;
    ans.push(num);
    DFS(num * 2);
    DFS(num * 2 +1);
  }
  DFS(1);
  console.log(ans.join(' '));
}

pre();

const mid = () => {
  let ans = [];
  // 왼쪽 자식 : 본인 * 2 
  // 오른쪽 자식 : 본인 * 2 + 1
  const DFS = (num) => {
    if(num > 7) return;
    DFS(num * 2);
    ans.push(num);
    DFS(num * 2 +1);
  }
  DFS(1);
  console.log(ans.join(' '));
}

mid();

const post = () => {
  let ans = [];
  // 왼쪽 자식 : 본인 * 2 
  // 오른쪽 자식 : 본인 * 2 + 1
  const DFS = (num) => {
    if(num > 7) return;
    DFS(num * 2);
    DFS(num * 2 +1);
    ans.push(num);
  }
  DFS(1);
  console.log(ans.join(' '));
}

post();
const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const input = [];
rl.on('line', (line) => {
  input.push(line.trim());
}).on('close', () => {
  const [n, m] = input[0].split(' ').map(Number);
  const map = input.slice(1).map((line) => line.split(' ').map(Number));
  const chk = Array.from(Array(n), () => new Array(m).fill(false));

  const dy = [0, 1, 0, -1];
  const dx = [1, 0, -1, 0];

  function bfs(y, x) {
    let rs = 1;
    const q = [];
    q.push([y, x]);
    while (q.length) {
      const [ey, ex] = q.shift();
      for (let k = 0; k < 4; k++) {
        const ny = ey + dy[k];
        const nx = ex + dx[k];
        if (0 <= ny && ny < n && 0 <= nx && nx < m) {
          if (map[ny][nx] === 1 && !chk[ny][nx]) {
            rs += 1;
            chk[ny][nx] = true;
            q.push([ny, nx]);
          }
        }
      }
    }
    return rs;
  }

  let cnt = 0;
  let maxv = 0;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (map[i][j] === 1 && !chk[i][j]) {
        chk[i][j] = true;
        cnt += 1;
        maxv = Math.max(maxv, bfs(i, j));
      }
    }
  }

  console.log(cnt);
  console.log(maxv);
});
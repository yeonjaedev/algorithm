const [t,...arr] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n')
let cnt = 0;
while(cnt < 2*t){
  const [n,m] = arr[cnt].split(/\s/).map(Number)
  const tmp = arr[cnt+1].split(' ').map(Number)
  let array = new Array(n).fill(0).map(() => new Array(m));

  for(let i = 0; i<n; i++){
    for(let j=0; j<m; j++){
      array[i][j] = tmp[i*m+j]
    }
  }
  let dp = array
  for(let j = 1;j<m;j++){
      for(let i = 0;i<n;i++){
        dp[i][j] = dp[i][j] + Math.max(
          i == 0 ? 0 : dp[i-1][j-1],
          dp[i][j-1],
          i == n-1 ? 0 : dp[i+1][j-1] 
          )
      }
    }
  let result = 0
  for(let i=0;i<n;i++){
    result = Math.max(result,dp[i][m-1])
  }
  console.log(result)
  cnt += 2
}
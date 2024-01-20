const num = require('fs')
      .readFileSync('dev/stdin.txt', 'utf-8')
      .trim()
      .split('\n')
      .map(Number)
      .slice(1)


let dp = [1,2,4]
for(let i = 3;i<11;i++){
  dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
}
num.forEach(n=>{
  console.log(dp[n-1])
})


// N에 대해서 경우의 수를 찾을 때 우리는 1,2,3만 사용할 수 있으므로 다음 세가지 경우의 수가 있다.
// 1) (N-1)에서 1 더하기 -> dp[N-1]
// 2) (N-2)에서 2 더하기 -> dp[N-2]
// 3) (N-3)에서 3 더하기 -> dp[N-3]
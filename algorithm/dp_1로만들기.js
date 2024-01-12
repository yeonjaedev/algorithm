const num = parseInt(require('fs').readFileSync('/dev/stdin').toString())

let dp = [0,0]
dp[2] = 1
dp[3] = 1

for(let i = 4;i<=num;i++){
  dp[i] = Math.min(
    i%5 == 0 ? dp[Math.floor(i/5)] : 50000,
    i%3 == 0 ? dp[Math.floor(i/3)] : 50000,
    i%2 == 0 ? dp[Math.floor(i/2)] : 50000,
    dp[i-1]
  ) + 1
}
console.log(dp[num])
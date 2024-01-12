const [n, ...arr] = require('fs').readFileSync('/dev/stdin').toString().trim().split(/\s/).map(Number);

let dp = []

dp[0] = arr[0]
dp[1] = Math.max(arr[0],arr[1])
for (let i = 2;i<n;i++){
  dp[i] = Math.max(dp[i-1],dp[i-2]+arr[i])
}
console.log(dp[n-1])
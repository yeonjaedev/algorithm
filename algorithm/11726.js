const num = parseInt(require('fs').readFileSync('/dev/stdin', 'utf-8').trim())

dp = [1,2]
for(let i = 2; i<num; i++){
  dp[i] = (dp[i-1]+dp[i-2]) % 10007 
}
console.log(dp[num-1])


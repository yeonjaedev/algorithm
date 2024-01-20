const num = parseInt(require('fs')
      .readFileSync('dev/stdin.txt', 'utf-8')
      .trim())


let dp = [9]

for(let i = 1;i<num;i++){
  dp[i] = (dp[i-1]*2 -i)%1000000000
}
console.log(dp[num-1])
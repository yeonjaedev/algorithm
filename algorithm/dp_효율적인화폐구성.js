const [n,m,...arr] = require('fs').readFileSync('/dev/stdin').toString().trim().split(/\s/).map(Number)

let dp = [0]

for(let i = 1;i<=m;i++){
  dp[i] = 10000;
}

for(let i =0;i<=n;i++){
  let num = arr[i]
  for(let j = num;j<=m;j++){
    if(dp[j-num]<10000){
      dp[j] = Math.min(dp[j],dp[j-num]+1)
    }

  }
}

console.log(dp[m] == 10000 ? -1 :dp[m])
const arr = require('fs')
  .readFileSync('dev/stdin.txt', 'utf-8')
  .trim()
  .split('\n')
  .slice(1)
  .map((string) => string.split(' ').map(Number))[0]

let ans = 0
const reverseArr = arr.reverse()
let dp = new Array(reverseArr.length).fill(1)

for(let i = 1;i<reverseArr.length;i++){
  for(let j = 0;j<i;j++){
    if(reverseArr[j]<reverseArr[i]){
      dp[i] = Math.max(dp[i],dp[j]+1)
    }
  }
}
console.log(reverseArr.length - dp[dp.length-1])
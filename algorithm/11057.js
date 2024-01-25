const num = parseInt(require('fs').readFileSync('/dev/stdin', 'utf-8').trim());

let dp = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]];

for (let i = 0; i < num - 1; i++) {
    dp.push(new Array(10).fill(1));
}
for (let i = 1; i < num; i++) {
    for (let j = 1; j < 10; j++) {
        dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % 10007;
    }
}
let sum = 0;
for (i = 0; i < 10; i++) {
    sum = (sum + dp[num - 1][i]) % 10007;
}
console.log(sum % 10007);

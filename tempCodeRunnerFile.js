
    [0, 1],
    [1, 0],
    [2, 1],
];

for (let i = 3; i < num; i++) {
    dp[i] = [dp[i - 1][0] + dp[i - 1][1], dp[i - 1][0]];
}
console.log(dp);
// console.log(dp[num - 2][0] + dp[num - 2][1]);
let ans = num == 1 ? 1 : num == 3 ? 2 : dp[num - 2][0] + dp[num - 2][1];

console.log(ans);

let input = require('fs')
    .readFileSync('/dev/stdin', 'utf-8')
    .trim()
    .split('\n');

let num = parseInt(input[0]);
input = input.splice(1);

while (num) {
    let result = 0;
    let cnt = parseInt(input[0]);
    let arr = [];
    arr.push(input[1].split(' ').map(Number));
    arr.push(input[2].split(' ').map(Number));

    let dp = [[], []];
    dp[0][0] = 0;
    dp[1][0] = 0;

    dp[0][1] = arr[1][0] + arr[0][1];
    dp[1][1] = arr[0][0] + arr[1][1];

    for (let i = 2; i < cnt; i++) {
        dp[0][i] = Math.max(dp[1][i - 1], dp[1][i - 2]) + arr[0][i];
        dp[1][i] = Math.max(dp[0][i - 1], dp[0][i - 2]) + arr[1][i];
    }

    console.log('ans', Math.max(dp[0][cnt - 1], dp[1][cnt - 1]));
    let dp2 = [];
    for (let i = 0; i <= cnt; i++) {
        dp2.push([0, 0]);
    }
    dp2[1][0] = arr[0][0];
    dp2[1][1] = arr[1][0];
    for (let i = 2; i <= cnt; i++) {
        dp2[i][0] = Math.max(dp2[i - 1][1], dp2[i - 2][1]) + arr[0][i - 1] * 1;
        dp2[i][1] = Math.max(dp2[i - 1][0], dp2[i - 2][0]) + arr[1][i - 1] * 1;
    }
    // console.log(dp);
    // console.log(dp2);
    console.log('dp2 Ans', Math.max(...dp2[cnt]));
    input = input.splice(3);
    num -= 1;
}

const num = parseInt(require('fs').readFileSync('/dev/stdin', 'utf-8').trim());

let dp = [1, 1];
for (let i = 2; i < num; i++) {
    dp[i] = BigInt(dp[i - 2]) + BigInt(dp[i - 1]);
}
console.log(BigInt(dp[num - 1]).toString());

// 현재 result 내에 들어가는 수의 Type인 Number의 최대 값을 넘어서게 되어 Overflow가 발생

// Number가 아닌 BigInt 형을 사용하며 이러한 에러의 가능성을 없애주어야 하며
// 출력할 때는 Number와 달리 BigInt의 경우 마지막 자리에 n이 붙기 때문에 그대로 출력하지 않고 String 형으로 변환하여 출력해야한다.

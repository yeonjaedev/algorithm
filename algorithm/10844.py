#쉬운 계산 수
MOD = 1000000000

n = int(input())

cache = [[0]*10 for _ in range(101)]
for i in range(1,10):
  cache[1][i] = 1


for i in range(2,101):
  for j in range(10):
    if j > 0:
      cache[i][j] += cache[i-1][j-1]
      cache[i][j] %= MOD
    if j < 9:
      cache[i][j] += cache[i-1][j+1]
      cache[i][j] %= MOD




ans = 0
for j in range(10):
  ans += cache[n][j]
  ans %= MOD
print(ans)
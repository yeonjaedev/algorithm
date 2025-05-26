N,K = map(int,input().split())
print(N,K)
arr = [[0] * (N+1) for _ in range(N+1)]
arr[0][0] = 1
arr[1][0] = 1
arr[1][1] = 1
MOD = 10007
for i in range(2,N+1):
  for j in range(0,i+1):
    if i-1 > 0 and arr[i-1][j] :
      arr[i][j] = (arr[i-1][j-1] + arr[i-1][j]) % MOD
    else:
      arr[i][j] = 1
print((arr[N][K])%MOD)
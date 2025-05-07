import sys
mod = 10007
sys.setrecursionlimit(10**7)
N,K = map(int,input().split())

arr = [[0] * 1001 for _ in range(1001)]
arr[0][0] = 1

def bino(n,r):
  if arr[n][r]:
    return arr[n][r]
  if r==0 or n==r:
    arr[n][r] = 1
  else:
    arr[n][r] = bino(n-1,r-1) + bino(n-1,r)
  return arr[n][r]

print(bino(N,K)%mod)
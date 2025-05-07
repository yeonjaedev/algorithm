mod = 10007

N,K = map(int,input().split())

def bino(n,r):
  if r==0 or n==r:
    return 1
  return bino(n-1,r-1) + bino(n-1,r)

print(bino(N,K))
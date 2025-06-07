import sys
input = sys.stdin.readline   
N,M = map(int,input().split())
arr = [[''] * M  for _ in range(N)]

for i in range(N):
  arr[i] = input()

def calcNum (a,b):
  # W 시작 
  cntW = 0
  cntB = 0
  for i in range(a,a+8):
    for j in range(b,b+8):
      if i%2 == 0 :
        if j%2==0:
          if arr[i][j] != 'W':
            cntW += 1
          else:
            cntB += 1
        else:
          if arr[i][j] != 'B':
            cntW += 1
          else:
            cntB += 1
      else:
        if j%2==0:
          if arr[i][j] != 'B':
            cntW += 1
          else:
            cntB += 1
        else:
          if arr[i][j] != 'W':
            cntW += 1
          else: cntB += 1

  return min(cntW,cntB)

ans = 64
for i in range(N):
  for j in range(M):
    if i+8 <= N and j+8 <= M:
      ans = min(ans,calcNum(i,j))
print(ans)
from itertools import combinations
N,M = map(int,input().split())
max = 4*N*N*M
arr = [[0]*N for _ in range(N)]
for i in range(N):
  arr[i] = list(map(int,input().split()))
chicken = []
for i in range(N):
  for j in range(N):
    if arr[i][j] == 2:
      chicken.append((i,j))
combi = list(combinations(chicken, M))

def calcDistance(target):
  distance = 0
  for i in range(N):
    for j in range(N):
      if arr[i][j] == 1:
        d = max
        for x,y in target:
          d = min(d,(abs(i-x) + abs(j-y)))
        distance += d
  return distance
ans = max
for com in combi:
  ans = min(ans,calcDistance(com))
print(ans)



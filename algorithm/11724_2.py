import sys
sys.setrecursionlimit(10 ** 6) # 재귀 내려갈 수 있는 깊이가 최대 1000으로 제한이 있음 - 이를 해제하기 위해

input = sys.stdin.readline

N,M = map(int,input().split())
arr = [[0] * N for _ in range(N)]

for i in range(M):
  u,v = map(int,input().split())
  arr[u-1][v-1] = arr[v-1][u-1] = 1

ans = 0
checked = [False] * N

def dfs(n):
  for i in range(N):
    if arr[n][i] and not checked[i]:
      checked[i] = True
      dfs(i)

for i in range(N):
  if not checked[i]:
    ans += 1
    dfs(i)
print(ans)

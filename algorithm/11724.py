# 연결 요소의 개수
# https://www.acmicpc.net/problem/11724
# import sys

# sys.setrecursionlimit(10 ** 6)
# input = sys.stdin.readline

# N,M = map(int,input().split())
# print(N,M)
# adj = [[0]*N for _ in range(N)]
# for _ in range(M):
#   x,y = map(int,input().split())
#   adj[x-1][y-1] = adj[y-1][x-1] = 1 # 무방향은 양방향과 동일하여 대각선 쪽에도 넣어줘야 함

# for i in range(N):
#   print(adj[i])

# checked = [False] * N
# ans = 0

# def dfs(now):
#   for nxt in range(N):
#     if adj[now][nxt] and not checked[nxt]:
#       checked[nxt] = True
#       dfs(nxt)

# for i in range(N):
#   if not checked[i]:
#     checked[i] = True
#     ans += 1
#     dfs(i)

# print(ans)

import sys;
sys.setrecursionlimit(10 ** 6) # 재귀 내려갈 수 있는 깊이가 최대 1000으로 제한이 있음 - 이를 해제하기 위해

input = sys.stdin.readline # 여러 줄이 들어오는 경우 빠른 입출력 써줘야 함

N,M = map(int,input().split())
arr = [[0]*N for _ in range(N)]

for _ in range(M):
  x,y = map(int,input().split())
  arr[x-1][y-1] = arr[y-1][x-1] = 1


checked = [False] * N
ans = 0
def dfs(start):
  for nxt in range(N):
    if arr[start][nxt] and not checked[nxt]:
      checked[nxt] = True
      dfs(nxt)

for i in range(N):
  if not checked[i]:
    ans += 1
    dfs(i)

print(ans)
# 인접행렬
adj = [ [0] * 13 for _ in range(13)]
for i in range(13):
  print(adj[i])

adj[0][1] = adj[0][7] = 1
adj[1][2] = adj[1][5] = 1
# ... 다 넣어주어야 함


# 재귀 방법의 DFS 
def dfs(now):
  for nxt in range(13):
    if adj[now][nxt]:
      dfs(nxt)

dfs(0)
from collections import deque
# BFS queue 사용

def bfs():
  dq = deque()
  dq.append(0)
  while dq:
    now = dq.popleft()
    for nxt in range(13):
      if adj[now][nxt]:
        dq.append(nxt)

bfs()


# 길찾기
dx = (1,0,-1,0) # 튜플 - 값을 변경할 수 없는 리스트
dy = (0,1,0,-1)
checked = [[False]*100 for _ in range(100)]
print(checked)
N = int(input())

def isValidCoord(y,x):
  return 0 <= y < N and 0 <= x < N

def bfs(start_y,start_x):
  dq = deque()
  dq.append((start_y,start_x))
  while dp:
    y,x = dq.popleft()
    checked[y][x] = True
    for i in range(4):
      ny = y + dy[i]
      nx = x + dx[i]
      if isValidCoord(ny,nx) and checked[ny][nx] == False:
        dq.append((ny,nx))

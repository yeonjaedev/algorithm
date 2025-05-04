# from collections import deque
# N,M = map(int,input().split())

# maze = [list(map(int, input())) for _ in range(N)]

# dx = (1,0,-1,0)
# dy = (0,1,0,-1)

# def isValidCoord(x,y):
#   return 0<=x<M and 0<=y<N

# def bfs():
#   dq = deque()
#   chk = [[False]*M for _ in range(N)]
#   dq.append((0,0,1))
#   chk[0][0] = True
#   while dq:
#     y,x,d = dq.popleft()

#     if y == N-1 and x == M-1:
#       return d

#     for k in range(4):
#       ny = y + dy[k]
#       nx = x + dx[k]
#       if isValidCoord(nx,ny) and maze[ny][nx] and not chk[ny][nx]:
#         chk[ny][nx] = True
#         dq.append((ny,nx,d+1))

# print(bfs())

from collections import deque;
N,M = map(int,input().split())
arr = [list(map(int,input().strip())) for _ in range(N)]

def isInner(y,x):
  return 0<=y<N and 0<=x<M

dx = (1,0,-1,0)
dy = (0,-1,0,1)


print(arr)
checked = [[False]*M for _ in range(N)]
print(checked)

def bfs():
  dq = deque()
  dq.append((0,0,1))
  checked[0][0] = True
  while dq:
    y,x,d = dq.popleft()

    if y == N-1 and x == M-1:
      return d
    for i in range(4):
      ny = y+dy[i]
      nx = x+dx[i]
      if isInner(ny,nx) and arr[ny][nx] and not checked[ny][nx]:
        checked[ny][nx] = True
        dq.append((ny,nx,d+1))

print(bfs())





















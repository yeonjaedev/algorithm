import sys;
input = sys.stdin.readline

N,P = map(int,input().split())
arr = [[] for _ in range(6)]
ans = 0
for _ in range(N):
  x,y = map(int,input().split())
  while(arr[x-1] and arr[x-1][-1] > y):
    arr[x-1].pop()
    ans += 1
  if y in arr[x-1]:
    continue

  arr[x-1].append(y)
  ans += 1
print(ans)

 
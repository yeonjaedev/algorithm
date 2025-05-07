# 이진탐색
N = int(input())
arr = list(map(int,input().split()))
M = int(input())


low = 0
high = max(arr)
mid = (low + high) // 2
ans = 0

def isPossible(mid):
  return sum(min(i,mid) for i in arr) <= M

while(low <= high):
  if isPossible(mid):
    low = mid + 1
    ans = mid
  else:
    high = mid - 1
  mid = (low + high) // 2
print(ans)
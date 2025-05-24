N = int(input())
arr = list(map(int,input().split()))
M = int(input())

low = 0
high = max(arr)
mid = (low + high) // 2
ans = 0

def isPossible(num):
  return sum(min(i,num) for i in arr) < M 

while(low<=high):
  mid = (low+high)//2
  if isPossible(mid):
    low = mid + 1
    ans = mid
  else:
    high = mid - 1
print(ans)
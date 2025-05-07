from bisect import bisect_left,bisect_right
N = int(input())
s_arr = sorted(list(map(int,input().split())))
M = int(input())
num_arr = list(map(int,input().split()))

ans = []


def has_number(num):
  low = 0
  high = len(s_arr) - 1
  while(low <= high):
    mid = (low + high) // 2
    if s_arr[mid] == num:
      return True
    elif s_arr[mid] < num:
      # 찾는 값이 더 크니까 low를 키우기
      low = mid + 1
    else:
      # 찾는 값이 더 작으니까 high를 줄이기
      high = mid - 1
  return False


for i in num_arr:
  l = bisect_left(s_arr,i)
  r = bisect_right(s_arr,i)
  if r-l > 0:
  #if s_arr[bisect_left(s_arr,i)] == i:
    # 찾는 값이 있다면 
  #if has_number(i):
    ans.append('1')
  else:
    ans.append('0')
print(' '.join(ans))

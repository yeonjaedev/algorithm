N = int(input())
arr = list(map(int,input().split()))
M = int(input())
ans = 0
def calc_sum (num):
  sum = 0
  for i in arr:
    if i <= num:
      sum += i
    else:
      sum += num
  return sum
ans = 0
sum = 0
for i in range(int(M/N),M):
  tmp = calc_sum(i)
  if tmp > M or tmp == sum:
    break
  else:
    ans = i
    sum = tmp
print(ans)
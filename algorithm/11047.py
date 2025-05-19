N,K = map(int,input().split())
arr = []
for i in range(N):
  num = int(input())
  if num <= K:
    arr.append(num)
arr.sort(reverse=True)
ans = 0

for i in arr:
  if K // i > 0:
    ans += ( K // i )
    K -= (( K // i ) * i)
print(ans)
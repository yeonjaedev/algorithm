# https://www.acmicpc.net/problem/10870
# 피보나치 수 5

n = int(input())
arr = [0,1]
for i in range(2,n+1):
  arr.append(arr[i-2]+arr[i-1])
print(arr[n])
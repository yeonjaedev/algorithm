n = int(input())
mod = 10007
arr = [0] * (1001)
arr[1] = 1
arr[2] = 2
for i in range(3,n+1):
  arr[i] = (arr[i-1] + arr[i-2])%mod
print(arr[n]%mod)
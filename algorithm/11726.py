n = int(input())
cache = [0] * 1001
cache[0] = 0
cache[1] = 1
cache[2] = 2
mod = 10007
for i in range(3,1001):
  cache[i] = (cache[i-1] + cache[i-2])%mod

print(cache[n])


N = int(input())
arr = [0] * 1002
arr[0] = 0
arr[1] = 1
arr[2] = 2 
arr[3] = 3 
mod = 10007
# def f(n):
#   if arr[n]:
#     return arr[n]
#   else:
#     arr[n] = f(n-1) + f(n-2)
#   return arr[n]
for i in range(4,15):
  arr[i] = arr[i-1] + arr[i-2]
  print(i,arr[i])
print(arr[N]%mod)

n = int(input())
cache = [0] * 1001
cache[0] = 0
cache[1] = 1
cache[2] = 2
mod = 10007
for i in range(3,1001):
  cache[i] = (cache[i-1] + cache[i-2])%mod

print(cache[n])
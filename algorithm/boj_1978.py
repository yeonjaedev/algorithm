# https://www.acmicpc.net/problem/1978
# 소수찾기

n = int(input())
arr = list(map(int,input().split()))
answer = 0

def isPrime(num):
  if num == 1: return False
  for i in range(2,int(num**(1/2)+1)):
    if num % i == 0: return False
  return True

for num in arr:
  if isPrime(num):
    answer += 1
    
print(answer)
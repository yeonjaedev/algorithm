# arr = [0,1,1]
# n = int(input())
# for i in range(n+1):
#   if(i>2):
#     arr.append(arr[i-1] + arr[i-2])
# print(arr[n])


cache = [-1] * 100
cache[0] = 0
cache[1] = 1

def f(n):
  if(cache[n] < 0):
    return f(n-1) + f(n-2)
  else:
    return cache[n]

# def f(n):
#   if(n == 0):
#     return 0
#   elif(n == 1):
#     return 1
#   return f(n-1)+f(n-2)

print(f(int(input())))
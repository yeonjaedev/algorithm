import heapq
import sys

input = sys.stdin.readline
heap = []
n = int(input())
for i in range(n):
  num = int(input())
  # print(num, heap)
  if num == 0 :
    if len(heap) > 0:
      res = heapq.heappop(heap)
      print(res[1])
    else:
      print(0)    
  else:
    heapq.heappush(heap,(abs(num),num))    

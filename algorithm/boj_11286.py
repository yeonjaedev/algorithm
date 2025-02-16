# https://www.acmicpc.net/problem/11286
# 절댓값 힙
import heapq;
import sys;
hq = []
n = int(input())
input = sys.stdin.readline
for _ in range(n):
    x = int(input())
    if x:
        heapq.heappush(hq, (abs(x), x))
    else:
        print(heapq.heappop(hq)[1] if len(hq) != 0 else 0)
import sys
import bisect



input = sys.stdin.readline
N = int(input())
s_card = sorted(list(map(int,input().split())))
M = int(input())
card_list = list(map(int,input().split()))
ans = []

for i in card_list:
  l = bisect.bisect_left(s_card,i)
  r = bisect.bisect_right(s_card,i)
  ans.append('0' if l-r == 0 else '1')

print(' '.join(ans))
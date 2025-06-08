cnt = 0
while(1):
  cnt += 1
  L,P,V = map(int,input().split())
  if L == 0 and P == 0 and V == 0:
    break
  ans = ( V // P ) * L + min(V % P,L)
  print(f'Case {cnt}: {ans}')
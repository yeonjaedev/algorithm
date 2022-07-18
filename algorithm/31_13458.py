# 띄어쓰기로 입력받아 배열에 넣기
# 띄어쓰기로 입력받아 int 처리하기
# python 올림

import math
n = int(input())
a = list(map(int,input().split()))
fgfgb,c = map(int,input().split())

res = n
for i in range(len(a)):
    people = a[i]-b
    if people > 0 :
        res += math.ceil(people/c)

print(int(res))

# b빼고 그게 0보다 클때만 계산하면 된다.
# 처음엔 res += math.ceil((a[i]-b)/c)
# 했었는데 a[i]-b가 0보다 작아지면 값이 올림한 값이 마이너스 값이 될 수가 있기 때문에
# 0보다 작아지면 수행하면 안된다.


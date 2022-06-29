# X
# 변수 출력 print('My name'+name,int(a))
# 숫자는 str()로 변환해서 출력해줘야 한다.
# print( str(int(a)))
# while문에서 index
# for문 index range for i in range(1, t+1):  # 1부터 t까지
# print(f`Case #{i}: {a+b}`)

num = int(input())
index = 0
while index < num:
    a,b = input().split()
    print('Case #'+str(index+1)+':',int(a)+int(b))
    index +=1
num = int(input())
for i in range(num):
    print(' '*(i)+'*'*((num*2)-(2*i+1)))
for i in range(num-1):
    print(' '*(num-i-2)+'*'*((i+1)*2+1))
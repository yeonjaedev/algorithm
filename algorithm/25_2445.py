num = int(input())
for i in range(num):
    print('*'*(i+1)+' '*((num*2)-(i+1)*2)+'*'*(i+1))
for i in range(num-1):
    print('*'*(num-i-1)+' '*((i+1)*2)+'*'*(num-i-1))
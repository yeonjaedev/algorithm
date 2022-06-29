num = int(input())
for i in range(num):
    print(' '*(num-i-1)+'*'+(' 'if i != num-1 else '*')*(2*i-1)+(' 'if i==0 else'*'))

N, num = map(int,input().split())
arr = []
for _ in range(N) :
    arr.append(int(input()))

arr = sorted(arr,reverse=True)
ans = 0
while(num > 0):
    for i in arr:
        if(i <= num):
            ans = ans + (num // i)
            num -= i * (num // i)

# for i in arr:
#     ans += num // i
#     ans %= i


print(ans)

# n = int(input())
#
# for _ in range(n):
#     str = input()
#     res = ''
#     sum = 0
#
#     for i in str:
#         if len(str) % 2 != 0:
#             sum = -1
#             break;
#         if i == '(':
#             sum += 1
#         elif i == ')' and sum <= 0:
#             sum = -1
#             break
#         else:
#             sum -= 1
#     res = ('YES' if sum == 0 else 'NO')
#     print(res)


for _ in range(int(input())):
    stack = []
    for ch in input():
        if ch == '(':
            stack.append(ch)
        else:
            if len(stack) <= 0:
                stack.append(ch)
                break
            else:
                stack.pop()

    print('YES' if len(stack) == 0 else 'NO')

# n = int(input())
# arr = []
# for _ in range(n):
#     arr.append(input())
#
# s = set()
# for i in arr :
#     s.add((i,arr.count(i)))
# print(max(sorted(s), key=lambda x: x[1])[0])

d = dict()
for _ in range(int(input())):
    book = input()
    d[book] = 1 if book not in d else d[book] + 1

maxValue = max(d.values())
arr = []
for i in d:
    if d[i] == maxValue:
        arr.append(i)

print(sorted(arr)[0])
N = int(input())
dict = {}
for i in range(N):
  book = input()
  if book in dict.keys():
    dict[book] = dict[book]+1
  else:
    dict[book] = 1
maxValue = max(dict.values())
ans = []
for item in dict.items():
  if item[1] == maxValue:
    ans.append(item[0])
print(sorted(ans)[0])

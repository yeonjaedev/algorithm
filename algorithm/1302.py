n = int(input())
dict = {}
for _ in range(n):
  book = input()
  if(book in dict):
    dict[book] = dict[book]+1
  else:
    dict[book] = 1

maxValue = max(dict.values())

ans = []
for book,count in dict.items():
  if count == maxValue:
    ans.append(book)
print(sorted(ans)[0])

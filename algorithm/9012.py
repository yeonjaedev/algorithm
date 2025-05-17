# 괄호

for i in range(int(input())):
  str = input()
  stack = []
  for ch in str:
    if ch == '(':
      stack.append(ch)
    else:
      if len(stack) <= 0:
        stack.append(ch)
        break
      stack.pop()
  print( 'YES' if len(stack) == 0 else "NO")
# if문 비교할 때 입력받은건 int로 변환하기
# 나머지 구하는 %
days = [31,28,31,30,31,30,31,31,30,31,30,31]
m,d = input().split()
num = 0
for i in range(len(days)):
    if i+1 == int(m):
        break
    num+=days[i]
num += int(d)
date = ['MON','TUE','WED','THU','FRI','SAT','SUN']
print(date[(num%7)-1])


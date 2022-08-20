# https://school.programmers.co.kr/learn/courses/30/lessons/12899
# 124나라의 숫자

def solution(n):
    answer = ''
    remainder = [] # 나머지
    while( n > 0) :
        a = n%3
        if not a:
            remainder.append('4')
            n-=1
        else:
            remainder.append(str(a))
        n = n//3
    for i in list(reversed(remainder)):
        answer += i
    return answer
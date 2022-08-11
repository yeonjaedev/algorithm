#https://school.programmers.co.kr/learn/courses/30/lessons/81301
# 숫자 문자열과 영단어
def solution(s):
    answer = ''
    dic = ['zero','one','two','three','four','five','six','seven','eight','nine']
    for i in dic:
        if i in s:
            s = s.replace(i,str(dic.index(i)))
    return int(s)
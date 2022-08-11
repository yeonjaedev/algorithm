# https://school.programmers.co.kr/learn/courses/30/lessons/70128
# 내적

def solution(a, b):
    answer = 0
    answer = sum(aNum * bNum for aNum,bNum in zip(a,b))
    return answer
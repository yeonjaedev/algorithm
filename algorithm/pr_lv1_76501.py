# https://school.programmers.co.kr/learn/courses/30/lessons/76501
# 음양더하기
def solution(absolutes, signs):
    answer = 0
    for i in range(len(signs)):
        answer += (1 if signs[i] else -1) * (absolutes[i])
    return answer
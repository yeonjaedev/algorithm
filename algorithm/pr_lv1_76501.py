# https://school.programmers.co.kr/learn/courses/30/lessons/76501
# 음양더하기
def solution(absolutes, signs):
    answer = 0
    for i in range(len(signs)):
        answer += (1 if signs[i] else -1) * (absolutes[i])
    return answer


# 한 줄로 다른 풀이
def solution(absolutes, signs):
    return sum(absolute if sign else -absolute for sign,absolute in zip(signs,absolutes))
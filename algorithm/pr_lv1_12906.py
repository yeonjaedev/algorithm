# https://school.programmers.co.kr/learn/courses/30/lessons/12906
# 같은 숫자는 싫어

# list 순회하며 pop하면 안됨 !

def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in arr:
        if i != answer[-1]:
            answer.append(i)
    return answer
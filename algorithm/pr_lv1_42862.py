#https://school.programmers.co.kr/learn/courses/30/lessons/42862
#체육복 Greedy 
def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    reserve.sort()
    for k in reserve[:]:
        if k in lost[:]:
            reserve.remove(k)
            lost.remove(k)
    answer = n - len(lost)
    for i in lost:
        if i-1 in reserve:
            reserve.remove(i-1)
            answer+=1
        elif i+1 in reserve:
            reserve.remove(i+1)
            answer+=1
    
    return answer
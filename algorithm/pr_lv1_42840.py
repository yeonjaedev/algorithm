import numpy as np

def solution(answers):
    answer = []
    res=[]
    person=[[1,2,3,4,5]*(len(answers)//5+1)
            ,[2,1,2,3,2,4,2,5]*(len(answers)//8+1)
            ,[3,3,1,1,2,2,4,4,5,5]*(len(answers)//10+1)]
    for i in range(3) :
        answer.append(list(np.equal(answers, person[i][0:len(answers)])).count(True))

    maxCnt = max(answer)
    for i in range(len(answer)):
        if answer[i] == maxCnt:
            res.append(i+1)
    return res


# 나머지 활용한 풀이
import numpy as np

def solution(answers):
    answer = [0,0,0]
    res=[]
    person=[[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    for i in range(len(answers)) :
        if answers[i] == person[0][i%len(person[0])]:
            answer[0] += 1
        if answers[i] == person[1][i%len(person[1])]:
            answer[1] += 1
        if answers[i] == person[2][i%len(person[2])]:
            answer[2] += 1
    maxCnt = max(answer)
    for i in range(len(answer)):
        if answer[i] == maxCnt:
            res.append(i+1)
    return res
    
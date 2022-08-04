import math
def solution(progresses, speeds):
    answer = []
    
    workDay = []
    for i in range(len(progresses)):
        workDay.append(math.ceil((100-progresses[i])/speeds[i]))
    i = 0
    while i < len(progresses):
        cnt = 1
        if i+1 == len(progresses):
            answer.append(cnt)
            break
        maxNum = workDay[i]
        while maxNum >= workDay[i+1]: # 이부분을 workDay[i] 로 처음에 풀이 했었음,, 앞뒤꺼의 크기만 비교하면 되는줄알고,, 그게 아니라 배포하는 날의 해당 값보다 작으면 됐던것 ,,,,!!!! > 문제 제대로 읽기
            cnt+=1
            i+=1
            if i == len(progresses)-1:
                break
        i+=1
        answer.append(cnt)
        
    return answer
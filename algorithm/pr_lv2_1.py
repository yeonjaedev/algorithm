def solution(priorities, location):
    answer = 0
    answer = location
    for i in range(len(priorities)):
        for m in range(len(priorities)):
            if priorities[0] < priorities[m]:
                priorities.append(priorities[0])
                del priorities[0]
                answer = len(priorities)-1 if answer == 0 else answer-1
                break
    return answer+1
import collections
def solution(participant, completion):
    answer = ''
    return list(collections.Counter(participant)-collections.Counter(completion))[0]


# 효율 에러난 코드   
def solution(participant, completion):
    answer = ''
    for i in completion:
        if i in participant:
            participant.remove(i)
    return participant[0]

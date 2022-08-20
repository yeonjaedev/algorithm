# https://school.programmers.co.kr/learn/courses/30/lessons/42888
# 오픈채팅방


def solution(record):
    answer = []
    info = {} # id info 정보 dictionary
    for i in record:
        if i.split()[0] == 'Enter':
            info[i.split()[1]]=i.split()[2]
        elif i.split()[0] == 'Change':
            info[i.split()[1]]=i.split()[2] # 변경되면 id info의 값을 비꾼다
    for i in record: # id info에서 id를 찾아 출력한다.
        if i.split()[0] == 'Enter':
            answer.append(info[i.split()[1]]+'님이 들어왔습니다.')
        elif i.split()[0] == 'Leave':
            answer.append(info[i.split()[1]]+'님이 나갔습니다.')
    return answer

# https://school.programmers.co.kr/learn/courses/30/lessons/67256
# 키패드 누르기

def solution(numbers, hand):
    answer = ''
    nowLeft = '*'
    nowRight = '#'
    keypad = [['1','2','3'],['4','5','6'],['7','8','9'],['*','0','#']]
    for i in numbers:
        if i in [1,4,7]:
            answer+='L'
            nowLeft = str(i)
        elif i in [3,6,9]:
            answer+='R'
            nowRight = str(i)
        else:
            answer+=sol(i,nowRight,nowLeft,hand)
            if sol(i,nowRight,nowLeft,hand)=='L':
                nowLeft = str(i)
            else:
                nowRight = str(i)
    return answer
def sol(num,nowRight,nowLeft,hand):
    now = [0,0]
    right = [0,0]
    left =[0,0]
    arr = [['1','2','3'],['4','5','6'],['7','8','9'],['*','0','#']]
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            #print(x,y)
            if str(num) == arr[x][y]:
                now =[x,y]
            if nowRight == arr[x][y]:
                right =[x,y]
            if nowLeft == arr[x][y]:
                left =[x,y]
    rightDistance = abs(now[0]-right[0])+abs(now[1]-right[1]) # 현위치와 오른손위치 거리
    leftDistance = abs(now[0]-left[0])+abs(now[1]-left[1]) # 현위치와 왼손위치 거리
    #print(nowLeft,nowRight,num,hand,rightDistance,leftDistance)
    if rightDistance == leftDistance:
        return 'R' if hand == 'right' else 'L'
    elif rightDistance > leftDistance:
        return 'L'
    else:
        return 'R'

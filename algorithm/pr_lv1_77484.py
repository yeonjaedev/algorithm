# https://school.programmers.co.kr/learn/courses/30/lessons/77484
# 로또의 최고순위와 최저순위

def solution(lottos, win_nums):
    answer = [0,0]
    rank = list(range(6, 0, -1))
    print(rank)
    zeroCnt = 0
    equalCnt = 0
    for i in lottos:
        if i == 0:
            zeroCnt += 1
        else:
            for m in win_nums:
                if i == m:
                    equalCnt += 1
    answer[0] = rank.index(1 if zeroCnt+equalCnt==0 else zeroCnt+equalCnt)+1
    answer[1] = rank.index(1 if equalCnt==0 else equalCnt)+1
    return answer


    # 개선 코드
def solution(lottos, win_nums):
    answer = [0,0]
    rank = [6,6,5,4,3,2,1]
    print(rank)
    zeroCnt = 0
    equalCnt = 0
    for i in lottos:
        if i == 0:
            zeroCnt += 1
        else: # 2중포문 돌릴 필요 없음
            if i in win_nums:
                equalCnt += 1
    # 6개맞으면 1등이니까 rank[6]은 1 
    return rank[zeroCnt+equalCnt],rank[equalCnt]
    
#https://school.programmers.co.kr/learn/courses/30/lessons/86491
# 최소직사각형

#개선코드
def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)
# 둘중 큰것 중 제일 큰 요소 * 둘중 작은것 중 제일 큰 요소

def solution(sizes):
    answer = 0
    maxX = 0
    maxY = 0
    for i in sizes:
        if i[0] < i[1]:
            maxX = max(i[1],maxX)
            maxY = max(i[0],maxY)
        else :
            maxX = max(i[0],maxX)
            maxY = max(i[1],maxY)
    answer = maxX * maxY
    return answer
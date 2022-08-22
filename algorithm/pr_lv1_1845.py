# https://school.programmers.co.kr/learn/courses/30/lessons/1845
# 포켓몬

# set 활용
def solution(nums):
    #return len(set(nums)) if len(set(nums)) < len(nums)//2 else len(nums)//2
    return min(len(set(nums)),len(nums)//2)


def solution(nums):
    length = len(nums)//2 #개수
    uniqueArr = []
    for i in nums:
        if i not in uniqueArr:
            uniqueArr.append(i)
    return len(uniqueArr) if len(uniqueArr) < length else length

# https://school.programmers.co.kr/learn/courses/30/lessons/12977
# 소수 만들기

from itertools import combinations
def solution(nums):
    answer = 0
    # for i in range(len(nums)-2):
    #     for j in range(i+1,len(nums)-1):
    #         for k in range(j+1,len(nums)):
    #             if isPrimeNum(nums[i],nums[j],nums[k]):
    #                 answer += 1
    comList = list(combinations(nums,3))
    for i in comList:
        if isPrimeNum(i[0],i[1],i[2]):
            answer += 1
    return answer
def isPrimeNum(num1,num2,num3):
    sum = num1+num2+num3
    for i in range(2,sum//2+1):
        if sum%i == 0:
            return False
    return True
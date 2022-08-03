#https://school.programmers.co.kr/learn/courses/30/lessons/92334
# LV1 신고결과받기
from collections import Counter

def solution(id_list, report, k):
    answer = []
    cnt = []
    stoper= []
    report = list(set(report)) # 중복 요소 제거 
    for i in report:
        stoper.append(i.split(' ')[1])
    cnt = Counter(stoper)
    stoper =[]
    for n in range(len(id_list)):
        answer.append(0)
        if cnt[id_list[n]]>=k:
            stoper.append(id_list[n])
    for m in range(len(report)):
        for x in stoper:
            if arr[m][1] == x:
                answer[id_list.index(arr[m][0])] += 1
    for m in report:
        if cnt[m.split()[0]] >= k:
            answer[id_list.index(m.split()[0])] += 1
    return answer


# from collections import Counter

# def solution(id_list, report, k):
#     answer = []
#     arr = []
#     cnt = []
#     stoper= []
#     report = list(set(report)) # 중복 요소 제거 
#     for i in report:
#         arr.append(i.split(' '))
#         stoper.append(i.split(' ')[1])
#     cnt = Counter(stoper)
#     # stoper =[]
#     # for n in range(len(id_list)):
#     #     answer.append(0)
#     #     if cnt[id_list[n]]>=k:
#     #         stoper.append(id_list[n])
#     # # for m in range(len(arr)):
#     # #     for x in stoper:
#     # #         if arr[m][1] == x:
#     # #             answer[id_list.index(arr[m][0])] += 1
#     for m in report:
#         if cnt[m.split()[1]] >= k:
#             answer[id_list.index(m.split()[0])] += 1
#     return answer

# # def solution(id_list, report, k):
# #     answer = [0] * len(id_list)    
# #     reports = {x : 0 for x in id_list}
# #     print(reports)
# #     print(set(report))
# #     for r in set(report):
# #         reports[r.split()[1]] += 1
        
# #     for r in set(report):
# #         if reports[r.split()[1]] >= k:
# #             answer[id_list.index(r.split()[0])] += 1

# #     return answer

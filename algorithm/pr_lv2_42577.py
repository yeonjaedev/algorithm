# https://school.programmers.co.kr/learn/courses/30/lessons/42577
# 전화번호 목록
# 효율성, 정렬필요, 한단어가 다른거에 전체 다 들어가야함


def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if len(phone_book[i]) < len(phone_book[i+1]):
            if phone_book[i + 1][:len(phone_book[i])] == phone_book[i]:
                answer = False
                break
    return answer


# def solution(phone_book):
#     answer = True
#     phone_book.sort(key=len)
   
#     for i in range(len(phone_book)-1):
#         j+=1
#         while(j<len(phone_book)):
#             if phone_book[i] == phone_book[j][:len(phone_book[i])]:
#                 return False
#             j+=1
#     return True
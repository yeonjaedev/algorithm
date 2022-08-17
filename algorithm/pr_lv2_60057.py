# https://school.programmers.co.kr/learn/courses/30/lessons/60057
# 문자열 압축


def solution(s):
    answer = s
    co = ''
    for i in range(1,len(s)//2+1):
        tmp = s[0:i]
        count = 1
        for j in range(i,len(s)+i,i):
            #print(j,i)
            
            if s[j:j+i] == tmp:
                count += 1
            else:
                if count == 1:
                    co+=tmp
                else:
                    co+=str(count)+tmp
                tmp=s[j:j+i]
                count = 1
        answer=co if len(co)<len(answer) else answer
        co = ''
    return len(answer)


# def solution(s):
#     answer = s
#     length = 1
#     iter = 0
#     compression = ''
#     while(length <= len(s)//2):
#         iter = 0
#         while( iter < len(s)):
#             if iter >= length and compression[iter-length:iter] == s[iter:iter+length]:
#             #if len(compression) >= length and compression[len(compression)-length:len(compression)] == s[iter:iter+length]:
#                 if compression[iter-length-1].isdigit():
#                     compression = (compression[:iter-length-1] + (str(int(compression[iter-length-1])+1))  + compression[iter-length:])
#                 else :
#                     compression = (compression[:iter-length] + '2' + compression[iter-length:])
#             else:
#                 compression += s[iter:iter+length]
#             iter+=length
            
#         answer = compression if len(compression) < len(answer) else answer
#         compression = ''
#         length+=1
        
#     return len(answer)
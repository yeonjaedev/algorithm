def solution(numbers):
    answer = '0'
    numbers.sort(key=lambda num: str(num)*3, reverse=True)       #2. number는 1000이하의 숫자이므로 x3(반복)한 값으로 비교
    for i in numbers:
        answer += str(i)
    return str(int(answer))
   
########### 개념정리 ##########

#문자열 정렬 - 아스키코드 값 ( 숫자값 비교가 아니라 맨 앞글자로 비교 )
#print(sorted(['30','2','66666','1']))

#sort함수, sorted함수

#dictionary

#dictionary 정렬
dictlist = [
    {'height' : 170, 'weight': 60, 'name':'홍길동'},
    {'height' : 160, 'weight': 90, 'name':'이몽룡'},
    {'height' : 165, 'weight': 55, 'name':'성춘향'},
    {'height' : 180, 'weight': 70, 'name':'대조영'},
    {'height' : 180, 'weight': 85, 'name':'김개똥'},
    {'height' : 165, 'weight': 65, 'name':'아무개'}
    
]
 
# height 높은 순, weight 낮은 순
sorted_dict = sorted(dictlist, key = lambda x : (-x['height'], x['weight']))


#tuple
#>>> t1 = (1, 2, 'a', 'b')
#>>> t1[0]
#1

#python type 확인 type([2,3,4])

# 조합구하기
#https://ourcstory.tistory.com/414

#자리수 ( 십의자리수인지, 백자리수인지 )
# a = 103434
# len(str(a)) // 6



# [x*3 for x in numbers] 활용
# info = {x : x/pow(10,len(str(x))-1) for x in numbers} 




# 두번째 풀이
from itertools import permutations
def solution(numbers):
    answer = '0'
    #info = {x : x/pow(10,len(str(x))-1) for x in numbers} 
    info = {x : ((x*1111111)/1000000 if len(str(x))-1 == 0 else x/pow(10,len(str(x))-1)) for x in numbers} 
    sorted_dict = sorted(info.items(), key = lambda item: -item[1])
    print(sorted_dict)
    for i in sorted_dict:
        answer += str(i[0])
    return str(int(answer))
   

# 세번째 풀이
from itertools import permutations
def solution(numbers):
    answer = '0'
    arr = sorted(numbers,key=func(numbers[0],numbers[1]))
    # tmp = ''
    # pm = list(permutations(numbers, len(numbers)))
    # for i in pm:
    #     for k in range(len(numbers)):
    #         tmp +=str(i[k])
    #     print(tmp)
    #     answer = str(max(int(answer),int(tmp)))
    #     tmp =''
    return answer
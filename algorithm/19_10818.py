# X
# map함수를 사용해서 
# map : 두 번째 인자로 들어온 반복 가능한 자료형 ( list or tuple ) 을 첫번째 인자로 들어온 함수에 하나씩 집어넣어서 함수를 수행하는 함수
# map (적용시킬 함수, 적용할 값들)
n = int(input())
arr = list(map(int,input().split()))
# max = arr[0]
# min = arr[0]
# for i in arr[1:]:
#     if i > max:
#         max = i
#     elif i < min:
#         min = i
# print(min,max)
print(min(arr),max(arr))
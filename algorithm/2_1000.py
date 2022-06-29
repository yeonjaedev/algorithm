# X
# int() 로 string to int
# input()으로 입력받으면 무조건 string
# split() 함수 : 빈 값이면 띄어쓰기 기준으로 분리, split(',') 가능

# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 첫째 줄에 A+B를 출력한다.


a,b= input().split()
print(int(a)+int(b))
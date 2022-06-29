# X
# 입력이 없으면 출력을 멈추는 코드를 짜라, 에러가 발생할 경우 멈추기
# try, except 문
while(True):
    try:
        a,b = input().split()
        print(int(a)+int(b))
    except:
        break

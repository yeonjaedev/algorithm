# X
# 몇번의 입력이 있었는지 전혀 정보가 주어지지 않아 try,except 구문을 통해 EOF에러발생시 break를 해줌
while True:
    try:
        print(input())
    except EOFError:
        break
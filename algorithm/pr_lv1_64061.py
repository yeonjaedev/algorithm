# https://school.programmers.co.kr/learn/courses/30/lessons/64061
# 크레인 인형뽑기 게임

def solution(board, moves):
    answer = 0
    basket = []
    for j in moves:
        for i in range(len(board)):
            if not board[i][j-1] == 0:
                if len(basket) > 0: # 바구니에 하나라도 들어와있다면 체크
                    if basket[len(basket)-1] == board[i][j-1]:
                        basket.pop(len(basket)-1) # remove쓰면 안됨 remove, pop 차이 명확히 하기
                        answer += 2
                    else:
                        basket.append(board[i][j-1])
                else:
                    basket.append(board[i][j-1])
                board[i][j-1] = 0
                break;
    return answer
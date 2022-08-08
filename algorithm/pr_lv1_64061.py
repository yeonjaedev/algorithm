def solution(board, moves):
    answer = 0
    basket = []
    for j in moves:
        for i in range(len(board)):
            if not board[i][j-1] == 0:
                if len(basket) >1:
                    print('basket',basket[len(basket)-1])
                    print('값',board[i][j-1])
                    if basket[len(basket)-1] == board[i][j-1]:
                        answer += 2
                    else:
                        basket.append(board[i][j-1])
                else:
                    basket.append(board[i][j-1])
                board[i][j-1] = 0
                break;
    # print(basket) 
    # arr = list(range(1,len(basket),2))
    # print(arr)
    # for i in range(len(basket)-1):
    #     for j in arr:
    #         if basket[i] == basket[i+j]
        # if basket[i] == basket[i+1]:
        #     answer += 2
        #     basket.remove(basket[i])
        #     basket.remove(basket[i+1])

    return answer
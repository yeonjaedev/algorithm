N,M,x,y,K = map(int,input().split())
# N : 세로크기
# M : 가로크기
# x, y : 주사위를 놓은 곳의 좌표
# K : 명령의 개수
dice = [0]*6
# 동, 서, 북, 남 - 배열 기준으로!!!!!!
# arr[0][0] arr[0][1]...
# 00 01
# 10 11
# 20 21
# 30 31
#이니까 동으로 가면 y에 +1
dx = [0,0,-1,1]
dy = [1,-1,0,0]

def diceFunc(cmd):
    if cmd == 1: # 동쪽
        dice[1],dice[3],dice[4],dice[5] = dice[4],dice[5],dice[3],dice[1]
    elif cmd == 2: #서쪽
        dice[1],dice[3],dice[4],dice[5] = dice[5],dice[4],dice[1],dice[3]
    elif cmd == 3: #북쪽
        dice[0],dice[1],dice[2],dice[3] = dice[1],dice[2],dice[3],dice[0] 
    elif cmd == 4: #남쪽
        dice[0],dice[1],dice[2],dice[3] = dice[3],dice[0],dice[1],dice[2] 


arr = [list(map(int, input().split())) for _ in range(N)]
order = list(map(int, input().split()))

for i in range(K):
    nx = x + dx[order[i]-1]
    ny = y + dy[order[i]-1]
    if(nx < 0 or nx > N-1 or ny < 0 or ny > M-1):
        continue
    else:
        x,y = nx, ny
        diceFunc(order[i])
        if(arr[x][y] == 0):
            arr[x][y] = dice[3]
        else:
            dice[3] = arr[x][y]
            arr[x][y] = 0
        print(dice[1])

# 2차원 배열 입력받기 정리
# continue
# 배열
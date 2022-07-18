N,M,x,y,K = map(int,input().split())
# N : 세로크기
# M : 가로크기
# x, y : 주사위를 놓은 곳의 좌표
# K : 명령의 개수
dice = [0]*6
# 동, 서, 북, 남
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dice(cmd):
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
    x += dx[order[i]-1]
    y += dy[order[i]-1]
    print(str(x),str(y))
    # if(order[i]): # 지도 범위 체크

#2차원 배열 입력받기 정리

# 띄어쓰기 없이 주어진 숫자 입력을 배열에 넣기
# ( 입력을 한 글자씩 분리하여 리스트에 넣기 )
# 배열 반복문으로 입력받아 넣기
# append로 해야 배열형태로 들어감 그냥 gears+=list(map(int,input())) 하면 안됨
# 
gears = []
for _ in range(4):
    gears.append(list(map(int,input())))
cnt = int(input())
cmd = []
for _ in range(cnt):
    cmd.append(list(map(int,input().split())))
# 시계방향 회전
def clockwise(num):
    if num < 0 or num > 3:
        return
    arr = gears[num]
    tmp = arr[len(arr)-1]
    k = len(arr)-1
    while(len(arr)):
        if k == 0:
            break
        arr[k] = arr[k-1]
        k-=1
    arr[0] = tmp
    gears[num] = arr # 회전 후 gears에 세팅
    print(num+1, arr)
    if num + 1 <= 3:
        if gears[num+1][6] == gears[num][2] :
            anticlockwise(num+1)
    if num -1 >= 0:
        if gears[num-1][2] == gears[num][6] :
            anticlockwise(num-1)

# 반시계 방향 회전
def anticlockwise(num):
    if num < 0 or num > 3:
        return
    arr = gears[num]
    tmp = arr[0]
    for i in range(len(arr)-1):
        arr[i] = arr[i+1]
    arr[len(arr)-1] = tmp
    gears[num] = arr # 회전 후 gears에 세팅
    print(num+1, arr)
    if num + 1 <= 3:
        if gears[num+1][6] == gears[num][2] :
            clockwise(num+1)
    if num -1 >= 0:
        if gears[num-1][2] == gears[num][6] :
            clockwise(num-1)

for i in range(len(cmd)):
    if cmd[i][1] == 1:
        clockwise(cmd[i][0]-1)
    else :
        anticlockwise(cmd[i][0]-1)
print('최종',gears)
num = 0
for i in range(len(gears)):
    if gears[i][0] == 1:
        if i == 0:
            num +=1
        elif i == 1:
            num +=2
        elif i == 2:
            num +=4
        elif i == 3:
            num +=8
print(num)
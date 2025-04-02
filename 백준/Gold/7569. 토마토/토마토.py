import sys
from collections import deque
row, col, high = map(int, sys.stdin.readline().split())

box = [[[0]for _ in range(col)] for _ in range(high) ]

dx = [0,-1,0,1,0,0] #행의 움직임
dy = [1,0,-1,0,0,0] #열의 움직임
dz = [0,0,0,0,1,-1] #높이의 움직임

start = deque()

# box에 입력값을 넣으며 3차원 배열 채우기
for z in range(high):
    for y in range(col):
        box[z][y] = list(map(int, sys.stdin.readline().split()))

# box를 뒤지며 1인 애들 start라는 큐에 넣기
for z in range(high):
    for y in range(col):
        for x in range(row):
            if box[z][y][x] == 1:
                 start.append((z,y,x))

# bfs를 돌리며 시작지점에서 인접한 칸을 찾으며 거리로 날짜를 계산하는거 
def bfs(start):

    while start:
        z,y,x = start.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0<=nx <row and 0 <= ny < col and 0 <= nz < high:
                if box[nz][ny][nx]==0:
                    box[nz][ny][nx]= box[z][y][x]+1
                    start.append((nz,ny,nx))
bfs(start)

day =0
check = True
for z in range(high):
    for y in range(col):
        for x in range(row):
            if box[z][y][x] == 0:
                check = False    
                break
            day = max(day,box[z][y][x])
            
if check == False:
    print(-1)
else:
    print(day-1)
import sys
from collections import deque
row, col = map(int, sys.stdin.readline().split())
board = [list(map(str, sys.stdin.readline().strip())) for _ in range(row)]

dx = [0,-1,0,1]
dy = [1,0,-1,0]
d_go =[[0]*col for _ in range(row)]
d_water = [[float('inf')]*col for _ in range(row)]

water=[] 
for i in range(row):
    for j in range(col):
        if board[i][j] == "*":
            water.append((i,j))  #water이란 배열에 물이 시작되는 좌표들을 넣음


def bfs_water():
    visited = [[False]*col for _ in range(row)]
    que = deque()

    for x, y in water:      #물이 시작하는좌표에서 bfs를 돌리기 위해 큐에 넣고 방문처리 하는 과정
        que.append((x,y))
        visited[x][y] = True
        d_water[x][y] = 0 #시작 시간

    while que:
        x,y = que.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<= nx<row and 0<=ny<col:
                if board[nx][ny] != "X" and  not visited[nx][ny] and board[nx][ny]!= "D":    #물이 갈 수 있는곳에서만 큐에 넣자 
                    visited[nx][ny]=True
                    que.append((nx,ny))
                    d_water[nx][ny] = d_water[x][y]+1




#bfs
def bfs_go(start_x, start_y):
    visited = set()
    que = deque()
    que.append((start_x,start_y))
    visited.add((start_x,start_y))

    while que :
        x,y = que.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<= nx< row and 0<= ny <col:
                if board[nx][ny]!='X' and (nx,ny) not in visited and d_go[x][y]+1<d_water[nx][ny]:
                    que.append((nx,ny))
                    visited.add((nx,ny))
                    d_go[nx][ny] = d_go[x][y]+1
    
    do_x = do_y = None
    for i in range(row):
        for j in range(col):
            if board[i][j] =="D":
                do_x = i
                do_y = j
    if d_go[do_x][do_y]==0:
        print("KAKTUS")
    else:
        print(d_go[do_x][do_y])
start_x=start_y = None
for i in range(row):
    for j in range(col):
        if board[i][j] =="S":
            start_x = i
            start_y = j 
bfs_water()
bfs_go(start_x,start_y)

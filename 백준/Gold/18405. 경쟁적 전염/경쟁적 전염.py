import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())
gan=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
s, target_x,target_y = map(int,sys.stdin.readline().split())

dx = [0,-1,0,1]
dy = [1,0,-1,0]

# 초기 바이러스 위치 (번호, x, y)를 정렬해서 큐에 삽입
q = []
for i in range(n):
    for j in range(n):
        if gan[i][j] != 0:
            q.append((gan[i][j], i, j,0))       #0은 시간을 의미 / 초기 바이러스위치라
q.sort()    #번호 낮은 바이러스부터 bfs할 수 있도록 
q = deque(q)

while q:
    val, x, y, time = q.popleft()

    if time ==s:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<n and 0<= ny <n and gan[nx][ny] == 0:
            gan[nx][ny]= val
            q.append((val,nx,ny,time+1))            #bfs한번 돈거 즉 1초가 지났기에 time+1을 해줌

print(gan[target_x-1][target_y-1])

            

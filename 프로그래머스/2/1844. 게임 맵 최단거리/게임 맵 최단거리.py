from collections import *
def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[0]*m for _ in range(n)]
    que = deque()
    que.append((0,0))
    visited[0][0] = 1
    
    dx = [1,0,-1,0]
    dy = [0,-1,0,1]
    
    while que:
        x,y = que.popleft()
        if x==n-1 and y==m-1:
            return maps[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<= ny <m:
                if maps[nx][ny]==1 and not visited[nx][ny]:
                    maps[nx][ny] = maps[x][y] +1
                    visited[nx][ny] = 1
                    que.append((nx,ny))
    return -1


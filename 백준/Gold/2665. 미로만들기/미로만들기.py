import heapq, sys
n=int(sys.stdin.readline())
board = [list(map(int,sys.stdin.readline().strip())) for _ in range(n)]

dx = [0,-1,0,1]
dy = [1,0,-1,0]

#다익스트라 알고리즘
def da( x,y, v):
    inf = int(1e9)
    dis = [[inf]*v for _ in range(v)]
    dis[x][y] = 0
    que = []
    heapq.heappush(que,(0,x,y))

    while que : 
        cost,x,y = heapq.heappop(que)

        if cost > dis[x][y]:
            continue

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny <n:
                new_cost = cost+(1 if board[nx][ny] ==0 else 0)
                if new_cost < dis[nx][ny]:
                    dis[nx][ny] = new_cost
                    heapq.heappush(que,(new_cost,nx,ny))

    return dis[n-1][n-1]

print(da(0,0,n))
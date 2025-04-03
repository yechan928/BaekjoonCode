import sys
n = int(sys.stdin.readline())
board =[list(map(int,sys.stdin.readline().strip())) for _ in range(n)]
visited=[[False]*n for _ in range(n)]

dx = [0,-1,0,1]
dy = [1,0,-1,0]
danji = 0
def dfs(x,y):
    global danji
    visited[x][y]=True
    danji += 1

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if 0 <= nx < n and 0<= ny <n:
            if not visited[nx][ny] and board[nx][ny]==1 :
                dfs(nx,ny)
    return danji

result = []
count = 0
for i in range(n):
    for j in range(n):
        if board[i][j]==1 and not visited[i][j]:
            result.append(dfs(i,j))
            danji = 0
            count+=1

result.sort()
print(count)
for i in result:
    print(i)
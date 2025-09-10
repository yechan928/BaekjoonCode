import sys
from collections import deque


n, m = map(int, sys.stdin.readline().split())
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().strip())))

result = []

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

visited = [[0] * m for _ in range(n)]


def bfs(x, y):
    que = deque()
    que.append((x, y))
    visited[x][y] = 1

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 1 and visited[nx][ny] == 0:
                    board[nx][ny] = board[x][y] + 1
                    visited[nx][ny] = 1
                    que.append((nx, ny))
    return -1


bfs(0, 0)
print(board[n - 1][m - 1])

import sys

sys.setrecursionlimit(10**6)

t = int(sys.stdin.readline())
for _ in range(t):
    n, m, k = map(int, sys.stdin.readline().split())
    board = [[0] * n for _ in range(m)]
    visited = [[False] * n for _ in range(m)]

    for _ in range(k):
        u, v = map(int, sys.stdin.readline().split())
        board[v][u] = 1

    # 우, 상, 좌 ,하
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    count = 0

    def dfs(y, x):
        visited[y][x] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if board[ny][nx] and not visited[ny][nx]:
                    dfs(ny, nx)

    for i in range(m):
        for j in range(n):
            if board[i][j] and not visited[i][j]:
                dfs(i, j)
                count += 1
    print(count)

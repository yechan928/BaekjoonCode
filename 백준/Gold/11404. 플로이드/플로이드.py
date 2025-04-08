import sys
n = int(sys.stdin.readline()) #도시수
m = int(sys.stdin.readline())
inf = float('inf')
bus = [[inf]*(n+1) for _ in range(n+1)]

for _ in range(m):
    u, v, cost = map(int, sys.stdin.readline().split())
    bus[u][v]=min(cost, bus[u][v])

for i in range(1, n+1):
    bus[i][i]=0

for mid in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            bus[i][j] = min(bus[i][j], bus[i][mid]+bus[mid][j])

for i in range(1,n+1):
    for j in range(1,n+1):
        if bus[i][j]==inf:
            print(0, end=' ')
        else:
            print(bus[i][j], end=' ')
    print()



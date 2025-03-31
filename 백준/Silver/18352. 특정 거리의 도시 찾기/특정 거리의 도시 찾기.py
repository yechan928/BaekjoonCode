import sys 
from collections import deque
n, m, k, x = map(int,sys.stdin.readline().split())
graph =[[] for _ in range(n+1)]
for _ in range(m):
    u,v = list(map(int, sys.stdin.readline().split()))
    graph[u].append(v)

result = []
distance = [-1]*(n+1)
distance[x]=0
#bfs
def bfs(graph,start):
    visited = set()
    que = deque([start])
    visited.add(start)

    while que:
        node = que.popleft()

        for neighbor in graph[node]:
            if neighbor not in visited:
                que.append(neighbor)
                visited.add(neighbor)
                distance[neighbor]= distance[node]+1

bfs(graph,x)

for i in range(1,n+1):
    if distance[i]==k:
        result.append(i)

result.sort()

if not result:
    print(-1)
for i in result:
    print(i)

import sys 
sys.setrecursionlimit(10**6)

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u,v = list(map(int,sys.stdin.readline().split()))
    graph[u].append(v)
    graph[v].append(u)

visited=[False]*(n+1)

#dfs
def dfs_recursive(graph,node,visited):
    visited[node] = True

    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs_recursive(graph,neighbor,visited)

count = 0


for i in range(1,n+1):
    if visited[i]==False:
        dfs_recursive(graph,i,visited)
        count +=1

print(count)
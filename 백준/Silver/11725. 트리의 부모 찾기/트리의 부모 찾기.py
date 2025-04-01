import sys
n = int(sys.stdin.readline())
graph = [[]for _ in range(n+1)]
for _ in range (n-1):
    u,v = list(map(int, sys.stdin.readline().split()))
    graph[u].append(v)
    graph[v].append(u)
parent = [0]*(n+1)
visited = [False]*(n+1)

#dfs
def dfs_stack(graph,start,visited):
    stack = [start]
    visited[start] = True

    while stack:
        node = stack.pop()
        
        for neighbor in graph[node]:
            if not visited[neighbor] :
                visited[neighbor] = True
                parent[neighbor] = node #부모기록
                stack.append(neighbor)

    return parent

dfs_stack(graph,1,visited)
for i in range(2,n+1):
    print(parent[i])
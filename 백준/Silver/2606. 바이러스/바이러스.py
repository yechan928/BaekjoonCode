import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph =[[] for _ in range(n+1)]
for _ in range(m):
    u,v = list(map(int, sys.stdin.readline().split()))
    graph[u].append(v)
    graph[v].append(u)

# print(graph[1])
# neighbor = []
# for i in graph[1]:
#     neighbor.append(graph[i])
visited=[False]*(n+1)
result = []
#dfs
def dfs_recursive(graph,node, visited):
    visited[node] = True
    result.append(node)
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs_recursive(graph,neighbor,visited)

dfs_recursive(graph,1,visited)
print(len(result)-1)
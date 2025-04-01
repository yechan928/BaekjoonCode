import sys, heapq
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[]for _ in range(n+1)]
for _ in range(m):
    u,v, w = list(map(int, sys.stdin.readline().split()))
    graph[u].append((w,v))

def dijkstar(graph, start,end, v):
    inf = int(1e9)
    distance = [inf]*(v+1)
    distance[start] = 0
    que = []
    heapq.heappush(que,(distance[start],start))

    while que:
        w, node = heapq.heappop(que)

        if w > distance[node]:
            continue
        for cost, neighbor in graph[node]:
            new_dist = w+cost

            if new_dist <distance[neighbor]:
                distance[neighbor]=new_dist
                heapq.heappush(que,(new_dist,neighbor))
    
    return distance[end]
start, end = map(int, sys.stdin.readline().split())
print(dijkstar(graph,start,end,n))
import sys
from collections import deque

input = sys.stdin.read
data = input().split()
index = 0

t = int(data[index])
index += 1
results = []

def bfs(start):
    queue = deque([start])
    color[start] = 1  # 시작 노드를 1로 색칠
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if color[neighbor] is None:  # 아직 방문하지 않은 경우
                color[neighbor] = 1 - color[node]  # 다른 색으로 칠함
                queue.append(neighbor)
            elif color[neighbor] == color[node]:  # 인접 노드가 같은 색이면 이분 그래프가 아님
                return False
    return True

for _ in range(t):
    n = int(data[index])
    m = int(data[index + 1])
    index += 2
    graph = [[] for _ in range(n + 1)]
    color = [None] * (n + 1)
    is_bipartite = True

    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        index += 2
        graph[u].append(v)
        graph[v].append(u)

    for i in range(1, n + 1):
        if color[i] is None:  # 아직 방문하지 않은 노드에 대해 BFS 수행
            if not bfs(i):
                is_bipartite = False
                break

    results.append("YES" if is_bipartite else "NO")

print("\n".join(results))

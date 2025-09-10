import sys
from collections import deque

n, m, k = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
visited = [False] * (n + 1)
result1 = []
result2 = []

for i in range(n + 1):
    graph[i].sort()


def dfs_recursive(node):
    visited[node] = True
    result1.append(node)
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs_recursive(neighbor)


def bfs(start):
    visited = set()  # 방문한 노드를 기록할 집합
    queue = deque([start])  # 시작 노드를 큐에 넣고 시작
    visited.add(start)  # 시작 노드 방문 처리

    while queue:
        node = queue.popleft()  # 큐에서 노드하나꺼냄(현재 탐색할 노드)
        result2.append(node)

        for neighbor in graph[node]:  # 현재 노드의 인접 노드들을 순회
            if neighbor not in visited:  # 아직 방문하지 않은 노드이면
                queue.append(neighbor)  # 큐에 추가하여 다음에 탐색할 수 있도록 함
                visited.add(neighbor)  # 방문 처리


dfs_recursive(k)
bfs(k)
print(*result1)
print(*result2)

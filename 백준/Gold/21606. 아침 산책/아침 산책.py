import sys

n = int(sys.stdin.readline())
A = sys.stdin.readline().strip()

graph = [[] for _ in range(n+1)]
place = [0]*(n+1)                   # 실내인지 실외인지 판단하는 배열, 실내:1,실외:0
visited = [0]*(n+1)

for i in range(len(A)):
    if A[i] ==1:
        place[i+1]=1

for _ in range(n-1):            #트리에서 간선의개수  = 정점의 개수-1
    u, v = list(map(int, sys.stdin.readline().split()))
    graph[u].append(v)
    graph[v].append(u)


#dfs를 생각하자
def dfs(node):          # 한 트리내에서 실내 개수 세기
    res = 0
    for next_node in graph[node]:
        if place[next_node]==0:                 # 인접한 노드의 장소가 실외이면 
            if not visited[next_node] :         # 인접한 노드를 방문했는지 확인하고 방문 안했으면
                visited[next_node]=1            # 방문했다고 체크해주고
                res += dfs(next_node)           # 재귀를 통해 연결된 실외 개수 탐색
        else:
            res += 1                            # 인접한 노드가 실내면  개수 +1
    return res 

ans = 0     # 최종 정답
for i in range(1, n+1):
    if place[i] ==0:                    # 현재 노드가 실외이면
        if not visited[i]:              # 아직 방문하지 않았으면
            visited[i] = 1              # 방문 표시 
            res = dfs(i)                # 이 실외 영역에 연결된  실내 노드 수 계산 
            ans += res*(res-1)          # 순열로 계산
    else:                               # 현재 노드가 실내면
        for next_node in graph[i]:      # 인접한 모든 노드 확인하고
            if place[next_node] ==1:    # 실내면 +1을 해라
                ans +=1

print(ans)
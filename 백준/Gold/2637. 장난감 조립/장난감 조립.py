import sys
from collections import deque

n = int(sys.stdin.readline())           # 완제품 번호
t = int(sys.stdin.readline())           #조립 정보 개수

parts = [[]for _ in range(n+1)]         # part[i]: i번 부품을 만들기 위한 정보
cnt = [0] * (n + 1)                     # cnt[i] = i번 부품이 필요한 개수
is_basic=[True]*(n+1)                   # 기본 부품 여부
indegree= [0]*(n+1)

for _ in range(t):
    x, y, k = map(int, sys.stdin.readline().split())
    parts[x].append((y,k))              # x를 만들기 위해 y가 k개 필요
    is_basic[x] = False
    indegree[y] += 1

cnt[n] = 1

#위상정렬
q = deque()
q.append(n)

while q:
    value = q.popleft()

    for part, num in parts[value]:
        cnt[part] += cnt[value]*num
        indegree[part] -= 1
        if indegree[part]==0:
            q.append(part)

# 기본 부품만 출력
for i in range(1, n + 1):
    if is_basic[i]:
        print(i, cnt[i])
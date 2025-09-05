import sys
from collections import deque

t = int(input())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    p = list(map(int, sys.stdin.readline().split()))
    q = deque()
    count = 0
    for i in range(n):
        q.append((i, p[i]))  # 큐에 인덱스와 그때의 중요도를 넣는다.

    while q:
        idx, priority = q.popleft()
        if q and priority < max(q, key=lambda x: x[1])[1]:
            q.append((idx, priority))
        else:
            count += 1
            if idx == m:
                print(count)
                break

import sys
import random

# 숫자마다 필요한 성냥개비 수
a = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
MAX = 100
match_cnt = [0] * MAX
# 수에 필요한 성냥 개수 구하기
# ex) 37 => 성냥 5+3 , 즉 8개의 성냥이 필요
for i in range(MAX):
    cnt = 0
    for j in str(i).zfill(2):
        cnt += a[int(j)]
    match_cnt[i] = cnt
n = int(sys.stdin.readline())
candi = []
for x in range(100):
    for y in range(100):
        z = x + y
        if z >= 100:
            continue
        if match_cnt[x] + match_cnt[y] + match_cnt[z] + 4 == n:
            candi.append(f"{str(x).zfill(2)}+{str(y).zfill(2)}={ str(z).zfill(2)}")
if candi:
    print(random.choice(candi))
else:
    print("impossible")

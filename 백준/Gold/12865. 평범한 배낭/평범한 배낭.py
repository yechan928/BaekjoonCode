import sys
from itertools import combinations

n ,k = map(int,sys.stdin.readline().split())
things = []

for _ in range(n):
    w,v = list(map(int,sys.stdin.readline().split()))
    things.append ((w,v))

# print(things)
#d[k] = max(d[k-w]+v,물건의 무게가 k일때의 v)
d=[0]*(k+1) #d[i] : 무게가 i일때 가질수 있는 최대 가치
for w, v in things:  # 각 물건을 한 번씩만 사용
    # 무게를 역순으로 순회 
    #(역순으로 안하면 무게가 중복해서 사용될 수 있다 . 왜냐 무게가 작은거부터 채워나가면 이미썼던걸 무게가 클때 또 사용할 수 있기에)
    for i in range(k, w - 1, -1):  
        d[i] = max(d[i], d[i - w] + v)  #점화식이 이런형식이기에 역순으로 돌아줘야함 왜냐 정순으로 돌면 작은거에 의해 중복될 수 있음

print(d[k])
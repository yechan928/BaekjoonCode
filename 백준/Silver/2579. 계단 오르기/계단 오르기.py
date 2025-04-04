import sys 
n = int(input())
s=[0]

for i in range(n):
    s.append(int(input()))

# 계단이 하나만 있는 경우는 예외 처리
if n == 1:
    print(s[1])
    exit()

D=[[0,0,0] for _ in range(n+1)]

D[1][1]=s[1]
D[1][2]=0
D[2][1]=s[2]
D[2][2]=s[1]+s[2]

for i in range(3,n+1):
    D[i][1] = max(D[i-2][1],D[i-2][2])+s[i]
    D[i][2] = D[i-1][1]+s[i]

print(max(D[n][1],D[n][2]))
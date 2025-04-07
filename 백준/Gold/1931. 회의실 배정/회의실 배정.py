import sys
n = int(sys.stdin.readline())
scehdule=[]
for _ in range(n):
    start, end = list(map(int, sys.stdin.readline().split()))
    scehdule.append((end,start))

scehdule.sort()
count = 0
t = 0

for end, start in scehdule:
    if t<=start:
        t = end
        count+=1

print(count)
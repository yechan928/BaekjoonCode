import sys

n = int(sys.stdin.readline())
a = []
for _ in range(n):
    a.append(list(map(int, sys.stdin.readline().split())))
b = []
if n >= 3:
    for i in range(n):
        if i == 0:
            c = (a[0][1] + a[0][2] - a[1][2]) // 2
            b.append(c)
        else:
            b.append(a[0][i] - c)
    print(" ".join(map(str, b)))
else:
    print("1 1")

# for i in b:
#     print(i, end=" ")

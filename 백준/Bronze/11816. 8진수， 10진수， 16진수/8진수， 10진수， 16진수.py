import sys

num = sys.stdin.readline()
if "0x" in num:
    n = int(num, 16)
    print(n)
elif num[0] == "0":
    k = int(num, 8)
    print(k)
else:
    m = int(num, 10)
    print(m)

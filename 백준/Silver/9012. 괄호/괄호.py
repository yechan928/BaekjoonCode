import sys

n = int(input())
for _ in range(n):
    m = sys.stdin.readline().strip()
    stack = []
    check = True

    for i in m:
        if i == "(":
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                check = False
                break

    if check and not stack:
        print("YES")
    else:
        print("NO")

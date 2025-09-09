import sys

n, k = map(int, sys.stdin.readline().split())
circle = [i for i in range(1,n+1)]
point = 0
result =[]
while circle:
    point = (point+k-1)%len(circle)  # 이거 때매 count없어도 됨
    result.append(str(circle.pop(point)))
print(f"<{', '.join(result)}>")

import sys
test = int(sys.stdin.readline())
result = []
for _ in range(test):
    n = int(sys.stdin.readline())
    grade = []
    for _ in range(n):
        a,b = list(map(int, sys.stdin.readline().split()))
        grade.append((a,b))
    grade.sort()
    count=1
    # print(grade)
    for i in range(n):
        if i ==0:
            min = grade[i][1]
            continue
        if grade[i][1]<min:
            min = grade[i][1]
            count+=1
    result.append(count)
for i in result:
    print(i)
# 히든넘버
import sys

n = int(sys.stdin.readline())
arr = sys.stdin.readline()
a = ""
num = []
for i in arr:
    if i.isdigit():
        a += i
    else:
        if a != "":
            num.append(int(a))
            a = ""
sum = 0
for i in num:
    sum += int(i)
print(sum)

# isdigit : 정수인지 아닌지 판단하는 함수
# a.isdigit -> false, 12.isdigit -> true

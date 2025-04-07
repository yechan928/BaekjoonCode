import sys

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))

#이진탐색
def binary_search(arr,key):
    pl = 0 
    pr = len(arr)-1

    while True:
        pc = (pl +pr)//2
        if arr[pc]==key:
            return pc
        elif arr[pc]<key:
            pl = pc+1
        else :
            pr = pc-1
        if pl>pr:
            return pl
#-------------------------------
result = []
for i in a:
    if len(result)==0:
        result.append(i)
        continue
    if result[-1] < i:
        result.append(i)
    else :
        result[binary_search(result,i)]=i

print(len(result))



import sys
sys.setrecursionlimit(10**9)
nums = []
while True:                            
    try:
        nums.append(int(sys.stdin.readline()))
    except:
        break

def huwin(arr):
    if len(arr)==0:
        return
    left=[]
    right=[]
    for i in range(1, len(arr)):
        if arr[0]<arr[i] :
            right.append(arr[i])
        else:
            left.append(arr[i])
    huwin(left)
    huwin(right)
    print(arr[0])

huwin(nums)

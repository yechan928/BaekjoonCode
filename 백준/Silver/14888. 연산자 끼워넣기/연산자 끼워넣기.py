import sys
n = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))
cal= list(map(int, sys.stdin.readline().split()))
exp=[]
max_val = int(-1e9)
min_val = int(1e9)

def dfs(depth, cal, exp): # cal : 연산자 배열, exp: 지금까지 선택한 연산자 순서
    global max_val, min_val
    if depth == n-1:
        result = nums[0]
        for i in range(n-1):
            op = exp[i]
            num = nums[i+1]
            if op == 0:
                result += num
            elif op ==1:
                result -= num
            elif op ==2:
                result *= num
            elif op==3:
                if result < 0:
                    result = -(-result//num)
                else:
                    result = result//num
        max_val = max(result,max_val)
        min_val = min(result,min_val)
    for i in range(4):          # 0:+,1:-,2:*,3:// 
        if cal[i]>0:
            cal[i]-=1
            exp.append(i)
            dfs(depth+1,cal,exp)
            exp.pop()
            cal[i]+=1

dfs(0,cal,exp)
print(max_val)
print(min_val)
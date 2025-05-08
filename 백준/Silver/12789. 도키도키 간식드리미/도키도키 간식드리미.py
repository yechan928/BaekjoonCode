import sys
n = int(sys.stdin.readline())
number_list =list(map(int,sys.stdin.readline().split()))
stack = []
current =1

# 사고 흐름
# 1. 줄 맨 앞 사람을 스택에 넣는다.
# 2. 스택의 top이 지금 필요한 번호(current)인지 확인한다.
#    -> 맞으면 꺼내서 보내고, current += 1
#    -> 계속 맞는 동안 꺼낸다.
# 3. 줄이 끝날 때까지 반복
# 4. while문 처리 후 스택 확인 후 

for num in number_list:    
    stack.append(num)
    while stack and stack[-1]==current:
        stack.pop()
        current += 1
if not stack:   # 스택이 비어있으면
    print("Nice")
else:           # 스택이 남아있으면
    print("Sad")
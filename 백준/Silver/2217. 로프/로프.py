import sys
n = int(sys.stdin.readline())
rope = [int(sys.stdin.readline()) for _ in range(n)]

rope.sort(reverse=True)
max_weight = 0
count = 1
for i in range(n):
    weight = rope[i]*count
    max_weight= max(max_weight,weight)
    # if i+1<n:               #인덱스 에러 날까봐
    #     if max_weight > rope[i+1]*(count+1):    # 다음 로프를 추가했는데 지금 무게 보다 적게나가면 
    #         break 
    count+=1
print(max_weight)
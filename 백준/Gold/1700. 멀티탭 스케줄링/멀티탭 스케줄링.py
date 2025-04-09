import sys
n, k = map(int, sys.stdin.readline().split())
sequence = list(map(int, sys.stdin.readline().split()))
concent=[]
#일단 opt(그리디)알고리즘을 사용해서 문제를 풀어보자
i = 0
# 콘센트에 초기 설정함
while (len(concent) < n and i <len(sequence)):
    # sequence[0]~[n-1]까지 중복된 값이 있다면 하나만 넣고 다음번째의 값을 플러그에 넣기
    if sequence[i] not in concent:
        concent.append(sequence[i])
    i+=1

count = 0 #콘센트 교체 횟수
for j in range(i,k):
    max_index=0
    change = False
    
    # 다음 것이 콘센트 안에 있으면 넘어가기 
    if sequence[j] in concent:
        continue

    # concent안에 값들이 sequence 안에 다시 등장하지 않는다면...? 그 등장하지 않는 놈을 교체하자
    for idx in range(len(concent)):
        if concent[idx] not in sequence[j:]:
            concent[idx]=sequence[j]
            count+=1
            change = True
            break
    
    if change == True:
        continue            #위에서 교체가 됐으면 다음 루프 돌기 


    # concent안에 값들이 전부 sequence 뒤에 나오는 경우 
    for c in concent:
        index = sequence[j:].index(c)   #sequence[j:]중에서 content의 원소가 있는 있는 인덱스찾고 인덱스끼리 비교하며 누가 늦게 나오나 비교하는중
        real_index = j+index
        # max_index = max(real_index, max_index)
        #위에 max함수로 계산하면 오류를 나타낼수 있다함
        if real_index > max_index:
            max_index = real_index
            max_index_value = c
            

    con_index = concent.index(max_index_value)
    concent[con_index] = sequence[j]
    count +=1

print(count)
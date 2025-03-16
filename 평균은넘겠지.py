t = int(input()) # 테스트 개수
count = 0
sum =0
avg = 0
percent = 0
score=[]
for i in range(t):
    score = list(map(int,input().split())) #학생 수
    for j in range(1,len(score)):
        sum += score[j]
    avg = sum/score[0]
    for j in range(1,len(score)):
        if avg<score[j]:
            count += 1 
    percent = (count/score[0])*100
    print(round(percent,3),"%")
    count=0
    sum =0
    avg=0
    percent = 0


#반올림 하는 함수 round
# round(1.2345)        : 1
# round(1.2345,0)      : 1.0
# round(1.2345,1)      : 1.2
# round(1.2345,2)      : 1.23
# round(1.2345,3)      : 1.235

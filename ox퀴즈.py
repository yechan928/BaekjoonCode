n = int(input())
count = 0
score = 0
for i in range(n):
    test= list(input())
    for j in range(len(test)):
        if test[j] == "O":
            count += 1
        else :
            count = 0
        score += count
    print(score)
    count=0
    score=0   



##연속으로 오는 "O"값을 세는 변수가 필요함-> 그게 count라는 변수
# 그 count를 더하는 score라는 변수도 
# 하나 입력이 끝나면 count랑 score 초기화해주기
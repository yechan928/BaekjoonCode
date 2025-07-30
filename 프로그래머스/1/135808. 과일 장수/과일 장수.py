def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)    # 사과를 내림차순으로 정렬
    for i in range(m-1,len(score),m):
        answer += score[i]*m
    return answer
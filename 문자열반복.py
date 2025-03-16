t = int(input())  # 테스트 케이스 개수 입력

for i in range(t):
    a, b = input().split()  # a는 반복 횟수, b는 문자열
    a = int(a)  # a를 정수로 변환

    for j in b:  # b의 각 문자에 대해 반복
        print(j * a, end="")  # 문자를 a번 반복하고 줄바꿈 없이 출력

    print()  # 테스트 케이스가 끝날 때 줄바꿈
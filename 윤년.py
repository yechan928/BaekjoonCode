year= int(input())
if (year%4==0 and year %100!=0) or year%400==0:
    print(1)
else:
    print(0)

#and는 논리 AND 연산자이고, 두개의 조건식이 모두 True일 때, True를 리턴
#&는 비트 연산자이며, 두개의 이진수에서 동일한 위치의 bit가 1인 것들만 1로 계산
#이건 비트연산자라 안됨
# year= int(input())
# if year%4==0 & year %100!=0 :
#     print(1)
# elif year %400 ==0:
#     print(1)
# else:
#     print(0)

# 우선순위 때문에 year % 4 == (0 & year % 100 != 0)와 같이 해석됨
#즉, 0 & year % 100 != 0 부분이 먼저 실행되어 논리가 잘못 될 수 있음
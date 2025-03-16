t = int(input()) #테스트 할 수 개수
numbers =list(map(int,input().split()))
# print(numbers)
def prime (list):
    count = 0
    for k in list:
        if k<2:
            continue
        else:              #list에서 숫자를 하나씩 가져옴
            for i in range(2,k):    #2부터 k-1까지 검사
                if k %i ==0:        #약수가 발견되면 break
                    break
            else:
                count += 1
    print(count)    
prime(numbers)


### 소수 인지 판단 하는 함수 만들기
# def prime_check(n):
#     if n == 1:  #  1은 소수가 아니므로 미리 처리
#         return False

#     for i in range(2, n):
#         if n % i == 0:  # 🔥 약수가 발견되면 소수가 아님
#             print(f'{n}은 소수가 아닙니다.')
#             return False

#     print(f'{n}은 소수입니다.')  # 🔥 for 루프가 끝까지 실행되면 소수
#     return True  # 소수일 경우 True 반환

# # 입력받아서 실행
# t = int(input())
# prime_check(t)


###위에 코드 다른 방법으로 해보기
# t = int(input())
# a = list(map(int,input().split()))
# def prime (list):
#     count = 0

#     for i in list:
#         if i == 1:
#             continue
#         prime_n = True

#         for j in range(2,i):
#             if i%j==0:
#                 prime_n = False
#                 break
#         if prime_n:
#             count+=1
#     return count
# print(prime(a))

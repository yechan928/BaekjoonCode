import math

t = int(input())
for i in range(t):
    # 주어진 수보다 작은 소수를 나열 하는 함수 
    def prime_list (c):
        primes=[] ##소수를 저장할 리스트
        a = [False,False] + [True]*(c-1)

        # for i in range(2, a):-----이거 시간이 오래 걸려서 안됨
        #     prime = True
        #     for j in range(2, int(math.sqrt(i))+1):
        #         if i%j ==0:
        #             prime  = False
        #             break
        #     if prime:
        #         primes.append(i)
        # return primes
        for i in range(2, c+1): #--에라토스테네스의 체 
            if a[i]:
                primes.append(i)
                for j in range(2*i, c+1, i):
                    a[j] = False
        return primes

    #소수인지 판단하는 함수
    def prime_check (b):
        if b==1:
                return False
        for i in range(2, int(math.sqrt(b)+1)):
            if b%i ==0:
                return False
        return True 
    
    test = int(input())

    primes = prime_list(test)

    p1, p2 = 0,0

    for i in primes :
        if prime_check(test-i):
            if p1==0 or abs(i-(test-i))<abs(p1-p2): #abs는 절대값구하는 함수
                p1 = i 
                p2 = test-i
    print(p1, p2)


#또 다른 방법
# import math

# def d(N): # 소수 판별 함수
#     if N == 1:
#         return False
#     for i in range(2, int(math.sqrt(N))+1):
#         if N % i == 0:
#             return False
#     return True
    
# N = int(input()) # 테스트 케이스 수 입력

# for _ in range(N):
#     num = int(input()) # 짝수 입력
    
#     A = num // 2 # 두 수 중 줄어드는 변수
#     B = num // 2 # 두 수 중 늘어나는 변수
    
#     for _ in range(num // 2):
#         if d(A) and d(B): # 두 수가 소수이면 출력
#             print(A, B)
#             break
#         else: # 소수가 아니면 두 수를 줄이고 늘리기
#             A -= 1
#             B += 1
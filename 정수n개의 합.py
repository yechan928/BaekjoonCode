a=[]
def solve(a):
    sum = 0
    for i in a:
        sum += i
    return sum
b = [1,2,3]
print(solve(b))
###파이썬에서 함수쓰기####

##함수 정의하는 방법
# def 함수이름 (매개변수1,..):
#   실행할 코드 
#   return 반환값

#간단한 예시
# def say_hello():
#    print("안녕하세요!")

# say_hello()  # 함수 호출----> 안녕하세요!
 
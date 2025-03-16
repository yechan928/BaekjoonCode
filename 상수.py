a, b= input().split()

def reverse (c):
    temp =""
    for i in c:
        temp = i+temp    #--기존에 있는 문자 앞에 계속 추가하는 형식
    return temp
# print(reverse(a), reverse(b))
max = reverse(a)
if reverse(b)>max : max = reverse(b)
print(max)

#다른 예시
#1. reversed()와 join()활용
# a = "hello"
# a ="".join(reversed(a))-- reversed는 문자열을 거구로 만든 iterator를 반환
#                                    따라서 join을 활용해 iterator를 문자열로 변환
# print(a) -->olleh

#2.슬라이싱 활용
# a = "hello"
# a = a[::-1]--문자열의 뒤에서 부터 읽어오는거 
# print(a) -->olleh
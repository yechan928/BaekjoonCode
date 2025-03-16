a = int(input())
b = int(input())
c = int(input())
d = a*b*c
d = str(d)#int에서 str으로 변환
# print(type(d))
for i in range(0,10):
    print(d.count(str(i)))

# count 함수
# 리스트나 문자열에서 특정 값이 몇번 등장하는 지 세는 함수 
# numbers = [1, 2, 3, 4, 2, 2, 5, 2]
# print(numbers.count(2))  # 2가 몇 번 나오는지 확인-->4


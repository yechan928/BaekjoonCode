B = int(input()) 
A=int(input())
temp1 = A//100
temp2 = (A%100)//10
temp3 = A%10

print (B*temp3)
print (B*temp2)
print (B*temp1)
print (B*A)

#궁금한거 
# 1.세자리수만 입력할 수 있게 할 순 없을지
# 2. temp를 너무 많이 써서 메모리 낭비가 됐을거 같은데 메모리를 줄이는 방법은?

# 궁금한거에 대한 해답 
# 배열을 사용해라 
# d = int(input())
# e = input()

# print(d*int(e[2]))
# print(d*int(e[1]))
# print(d*int(e[0]))
# print(d*int(e))
count = int(input())
result=[]
for i in range(0,count):
    a,b = map(int,input().split())
    result.append(a+b)
for i in result:
    print(i)

    
# 리스트에 값을 추가할 때는 append() 사용!
# 입력을 다 받고, 한 번에 출력하고 싶다면 리스트를 활용하면 됨!

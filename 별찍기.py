n = int(input())
for i in range(1,n+1):
    print("*"*i)
#문자열*숫자 하면 그만큼 더 찍힘
for i in range(1,n+1):
    print(" "*(n-i),"*"*i)
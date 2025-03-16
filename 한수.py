#한자리 수의 한 수 계산
n = int(input())
def su (x):
    if x<=99:
        print(x)
        return 
    count = 99
    for i in range(100, x+1):
        a = [int(d) for d in str(i)]# 세 자리 숫자를 정수형 리스ㅌ로 변환(리스트컴프리센션)
        # print(a)
        if (a[0]-a[1])==(a[1]-a[2]):
            count+=1
    print(count)
    
su(n)


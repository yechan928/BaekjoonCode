dan = int(input())
for i in range(1,10):
    print(dan,"*",i,"=",dan*i)

#for문 정리
#for 변수 in range(시작값, 끝값, 증감크기)
#변수가 시작값부터 (끝값-1)까지 증감크기의 간격으로 실행문을 실행함
#ex) for i in range(0,10,1)-> i는 0부터 9까지 1씩 증가하며 10번 시행됨
#ex) for i in range(값1)-> i는 0부터 (값-1)까지 1씩 증가하며 시행됨
#ex) for i in range(시작값, 끝값)-> 증가가 1씩 되는거 생략

# for 변수 in 객체 -> 여기서 객체는 문자열이나 리스트, 튜플, 딕셔너리를 의미함
# ex) for i in 'abc' -> i는 'a'부터 시작하여 'b','c'순으로 정의됨
# ex) for i in [1,2,3] -> i는 1부터 시작하여 2,3순으로 정의됨,
#numbers = [3, 5, 7, 2] 라면,
#for i in numbers:에서 i는 3 → 5 → 7 → 2 순서로 값이 됨
# ex) for i in {'one':1,'two':2,'three':3} -> i는 one부터 시작하여 two, three 순으로 정의됨

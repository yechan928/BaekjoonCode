n = int(input())   #원판 갯수
def hanoi_top (x):    #최소 이동수 
    if x>0:
        return 2*hanoi_top(x-1)+1
    else:
        return False
print(hanoi_top(n))
if n<=20:
    #움직이는 경로 
    def move(no, x,y):
        if no>1:
            move(no-1,x,6-x-y)
        print(x,y)
        if no>1:
            move(no-1,6-x-y,y)
        else:
            return False

    move(n,1,3)
else:
    pass
x,y,w,h =map(int,(input().split()))
min = x
if y<min:
    min = y
if w-x<min:
    min = w-x
if h-y<min:
    min = h-y
print(min)
#사실상 미니멈 구하기문제
#아래 방식으로도 가능
# if y<min :min=y
# if w-x<min :min=w-x
# if h-y<min :min=h-y
# print(min)
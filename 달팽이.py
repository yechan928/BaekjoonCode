import math
a,b,h = map(int,input().split())
c = h-a #전날 최소 올라가야하는 높이
d = a-b # 하루 올라가는 순수높이
print(math.ceil(c/d)+1) # ceil 소수를 올림하여 정수로 변환해주는 함수(math를 import할 것)
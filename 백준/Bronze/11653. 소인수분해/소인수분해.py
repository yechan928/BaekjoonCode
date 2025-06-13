import sys

n = int(sys.stdin.readline())
divisor = 2
while n > 1:
    if n % divisor == 0:
        n = n // divisor
        print(divisor)
    else:
        divisor += 1

import sys
n = int(sys.stdin.readline())

# def fibo (x):
#     if x==0:
#         return 0
#     if x==1:
#         return 1
#     return fibo(x-1)+fibo(x-2)

# print(fibo(n))

fi=[0]*(n+1)
fi[0] = 0
fi[1] = 1
for i in range(2,n+1):
    fi[i] = fi[i-1]+fi[i-2]

print(fi[n])
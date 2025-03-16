a=[]
b=[]
z=[]
w=[]

x,y = map(int,input().split())
a.append(0)
a.append(x)
b.append(0)
b.append(y)
#print(a,b)--[0,x],[0,y]
t = int(input())
for _ in range(t):
    c, d = map(int,input().split())
    if c==0:
        b.append(d)
    else:
        a.append(d)
    a.sort()
    b.sort()
for i in range(1,len(a)):
    z.append(a[i]-a[i-1])
for i in range(1,len(b)):
    w.append(b[i]-b[i-1])

print(max(z)*max(w))



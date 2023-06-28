n=int(input())
m1=[]
m2=[]
for i in range(n):
    a=list(map(int,input().split()))
    m1.append(a)
for i in range(n):
    b=list(map(int,input().split()))
    m2.append(b)
m3=[]
for i in range(n):
    x=[]
    for j in range(n):
        x.append(abs(m1[i][j]-m2[i][j]))
    m3.append(x)
for i in m3:
    print(*i)
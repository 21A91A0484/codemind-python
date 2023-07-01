r,c=map(int,input().split())
m=[]
for i in range(r):
    l=list(map(int,input().split()))
    m.append(l)
x=[]
for j in range(c):
    s=0
    for i in range(r):
        s+=m[i][j]
    x.append(s)
print(*x)
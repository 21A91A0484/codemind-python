r,c=map(int,input().split())
m=[]
for i in range(r):
    l=list(map(int,input().split()))
    m.append(l)
a=[]
for i in range(r):
    s=0
    for j in range(c):
        s+=m[i][j]
    a.append(s)
print(*a)
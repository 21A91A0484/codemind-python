n,m=map(int,input().split())
t=[]
for i in range(n):
    l=list(map(int,input().split()))
    t.append(l)
a=[]
for i in range(n):
    s=0
    for j in range(m):
        s+=t[i][j]
    a.append(s)
print(max(a))
n,m=map(int,input().split())
a=[]
for i in range(n):
    l=list(map(int,input().split()))
    a.append(l)
c=0
for i in a:
    x=i.copy()
    x.sort()
    if i==x or i==x[::-1]:
        c+=1
print(c)
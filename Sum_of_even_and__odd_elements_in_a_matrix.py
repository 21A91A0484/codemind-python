n,m=map(int,input().split())
m=[]
se=so=0
for i in range(n):
    a=list(map(int,input().split()))
    m.append(a)
    for i in a:
        if i%2==0:
            se+=i
        else:
            so+=i
print(se,so)

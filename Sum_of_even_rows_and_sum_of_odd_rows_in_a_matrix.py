a,b=map(int,input().split())
se=so=0
for i in range(a):
    r=list(map(int,input().split()))
    if i%2==0:
        se+=sum(r)
    else:
        so+=sum(r)
print(se,so)
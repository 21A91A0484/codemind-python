n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
x=[]
y=[]
for i in l:
    if i>=a and i<=b:
        x.append(i)
    else:
        y.append(i)
if x:
    print(max(x))
else:
    print(-1)
        
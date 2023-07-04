n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
x=[]
y=[]
for i in l:
    if(i<=b and i>=a):
        x.append(i)
    else:
        y.append(i)
if x:
    print(min(x))
else:
    print(-1)
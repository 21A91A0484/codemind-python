n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
x=[]
y=[]
for i in l:
    if(i>=a and i<=b):
        x.append(i)
    else:
        y.append(i)
s=0
for i in y:
    if i:
        s+=i
print(s)
        
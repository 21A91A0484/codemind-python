n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
x=[]
y=[]
for i in a:
    if i in b and i not in x:
        x.append(i)
for j in b:
    if j in a and j not in y:
        y.append(j)
print(len(x))
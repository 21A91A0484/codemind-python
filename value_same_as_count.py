n=int(input())
l=list(map(int,input().split()))
a=[]
for i in l:
    if l.count(i)==i and i not in a:
        a.append(i)
c=0
for k in a:
    if k:
        c+=1
print(c)
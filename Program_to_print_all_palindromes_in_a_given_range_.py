a = int(input())
b = int(input())
for i in range(a,b+1):
    rev=0
    temp=i
    while i>0:
        r=i%10
        i=i//10
        rev=rev*10+r
    if temp==rev:
        print(rev,end=' ')
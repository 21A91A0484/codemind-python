n=int(input())
l=list(map(int,input().split()))
a=set(l)
x=sorted(a)
if len(x)>=3:
    print(x[-3])
else:
    print(max(x))
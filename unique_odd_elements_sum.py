n=int(input())
l=list(map(int,input().split()))
ss=set(l)
s=0
for i in ss:
    if i%2!=0:
        s+=i
print(s)
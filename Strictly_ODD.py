n=int(input())
l=list(map(int,input().split()))
a=l[1::2]
b=[]
for i in a:
    if i%2!=0:
        b.append(i)
if len(a)==len(b):
    print("True")
else:
    print("False")
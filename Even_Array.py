a=int(input())
n=list(map(int,input().split()))
e=[]
for i in range(a):
    if n[i]%2==0:
        e.append(n[i])
if(len(n)==len(e)):
    print("True")
else:
    print("False")
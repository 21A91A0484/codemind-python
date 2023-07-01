n=int(input())
m1=[]
m2=[]
for i in range(n):
    a=list(map(int,input().split()))
    m1.append(a)
for j in range(n):
    b=list(map(int,input().split()))
    m2.append(b)
for i in range(n):
    for j in range(n):
        print(m1[i][j]+m2[i][j],end=' ')
    print()
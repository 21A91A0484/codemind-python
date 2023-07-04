n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    if l.count(i)>(n//2):
        c = i
print(c)
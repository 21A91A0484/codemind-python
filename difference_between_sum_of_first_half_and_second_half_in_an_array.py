n=int(input())
l=list(map(int,input().split()))
s1=s2=0
a=n//2
h1=l[:a]
h2=l[a:]
for i in h1:
    s1+=i
for j in h2:
    s2+=j
print(abs(s1-s2))

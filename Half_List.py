n=int(input())
l=list(map(int,input().split()))
a=n//2
h1=l[:a]
h2=l[a:]
x=h2[::-1]
print(*(x+h1))
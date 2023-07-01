s=input()
a=list(s)
for i in a:
    x=" ".join(s.split()[::-1])[::-1]
print(x)
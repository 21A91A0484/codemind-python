s=input()
l=list(s)
for i in l:
    x=" ".join(s.split(" ")[::-1])[::-1]
print(x)
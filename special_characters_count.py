s=input()
c=0
a=[]
b=[]
for i in s:
    if i.isalpha() or i in ' ':
        a.append(i)
    else:
        b.append(i)
for j in b:
    if b:
        c+=1
print(c)
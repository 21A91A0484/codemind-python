s=input()
c=0
for i in s:
    if i.isalpha() or i not in ' ':
        c+=1
print(c)
n=input()
s=0
for i in n:
    if i>='0' and i<='9':
        s=s+ord(i)-48
print(s)
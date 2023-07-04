s=input()
a=[]
for i in s:
    if i in 'aeiouAEIOU' and i not in a:
        a.append(i)
if a:
    print(*a)
else:
    print(-1)
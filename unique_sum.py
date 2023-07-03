n = int(input())
l = list(map(int,input().split()))
a = []
for i in l:
    if i not in a:
        a.append(i)
s=0
for j in a:
    if j in l:
        s+=j
print(s)
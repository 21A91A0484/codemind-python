s=input().lower()
st='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'
for i in s:
    if i not in st and i!=' ':
        st+=i
ss=sorted(st)
print(''.join(ss))

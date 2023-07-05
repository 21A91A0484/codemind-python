s=input()
v=input()
for i in s:
    if i in v:
        print("True")
        print(s.index(i))
        break
else:
    print("False")
    
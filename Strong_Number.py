n = int(input())
s = 0
temp = n
while temp>0:
    f = 1
    r = temp%10
    for i in range(1,r+1):
        f = f*i
    s+=f
    temp  = temp//10
if s==n:
    print("The number",n,"is a strong number")
else:
    print("The number",n,"is not a strong number")
        
        
a,b,c=map(int,input().split())
s=(a+b+c)/2
from math import sqrt
area=sqrt(s*(s-a)*(s-b)*(s-c))
print('%0.2f'%area)
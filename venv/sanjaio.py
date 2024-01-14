import math
x1,y1 = map(float,input().split())
x2,y2 = map(float,input().split())
x3,y3 = map(float,input().split())
a = math.sqrt((x1-x2)**2+(y1-y2)**2)
b = math.sqrt((x1-x3)**2+(y1-y3)**2)
c = math.sqrt((x2-x3)**2+(y2-y3)**2)
p = (a+b+c)/2
S = math.sqrt(p*(p-a)*(p-b)*(p-c))
print("%0.3f" %(S))
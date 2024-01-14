

x,y = map(int,input().split())
xpath = set()
while x>0:
    xpath.add(x)
    x = x//2
while y>0:
    if y in xpath:
        print(y)
        break
    else:
        y = y//2
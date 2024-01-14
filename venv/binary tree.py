import math
while True:
    m,n = map(int,input().split())
    if n == 0 and m == 0:
        break
    layer1 = int(math.log2(n+1))+(2**int(math.log2(n+1))!= n+1)
    layer2 = int(math.log2(m+1))+(2**int(math.log2(m+1))!= m+1)
    tag = layer1-layer2+1
    slice1 = 2**(tag-1)*m
    slice2 = (m+1)*2**(tag-1)-1
    alreadycount = 2**(tag-1)-1
    if n < slice1:
        print(alreadycount)
    elif n>slice2:
        print(2**tag-1)
    else:
        print(alreadycount+n-slice1+1)

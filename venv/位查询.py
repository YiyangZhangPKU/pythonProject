N,M = map(int,input().split())
numlist = list(map(int,input().split()))
for i in range(M):
    op,pos = input().split()
    if op == "Q":
        temp = [str(bin(x)[2:]).zfill(16) for x in numlist]
        count = 0
        i = int(pos)
        for binum in temp:
            if binum[-i-1] == "1":
                count += 1
        print(count)
    if op == "C":
        i = int(pos)
        for j in range(N):
            numlist[j] = (numlist[j]+1)%65535


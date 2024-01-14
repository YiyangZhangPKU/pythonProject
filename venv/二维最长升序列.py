r,c = map(int,input().split())
numlist =[]
for i in range(r):
    numlist.append(list(map(int,input().split())))
dp = [[0 for i in range(c)]for j in range(r)]
def LoogestPath(i,j):
    if dp[i][j] != 0:
        return dp[i][j]
    if i == 0 :
        up = 1
    elif numlist[i-1][j] >numlist[i][j]:
        up = 1
    else:
        up = dp[i-1][j]+1

    if i == r-1:
        down = 1
    elif numlist[i+1][j] >numlist[i][j]:
        down = 1
    else:
        down = dp[i+1][j]+1

    if j == 0:
        left = 1
    elif numlist[i][j-1] >numlist[i][j]:
        left = 1
    else:
        left =dp[i][j-1]+1

    if j == c-1:
        right = 1
    elif numlist[i][j+1] >numlist[i][j]:
        right = 1
    else:
        right = dp[i][j+1]+1
    dp[i][j] = max(up, down, left, right)
    return dp[i][j]

comp = []
Max = []
for i in range(r):
    for j in range(c):
        comp.append((numlist[i][j],i,j))
comp.sort(key=lambda x:x[0])
for ele in comp:
    LoogestPath(ele[1],ele[2])
for l in dp:
    Max.append(max(l))
print(max(Max))

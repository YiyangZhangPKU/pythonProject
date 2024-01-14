n = int(input())
mapgraph = []
for i in range(n):
    mapgraph.append(list(map(int,list(input()))))
flag = 0
first = []
second = []
def question(i,j,num):
    if mapgraph[i][j]!= 0 and mapgraph[i][j]!= num:
        return True
    else:
        return False
def dfs(i,j,num):
    mapgraph[i][j] = num
    if num == 2:
        first.append((i,j))
    else:
        second.append((i,j))
    if i != 0 and question(i-1,j,num):
        dfs(i-1,j,num)
    if i != n-1 and question(i+1,j,num):
        dfs(i+1,j,num)
    if j!=0 and question(i,j-1,num):
        dfs(i,j-1,num)
    if j!=n-1 and question(i,j+1,num):
        dfs(i,j+1,num)
for i in range(n):
    for j in range(n):
        if mapgraph[i][j] != 1:
            continue
        elif flag == 0:
            dfs(i,j,2)
            flag = 1
        else:
            dfs(i,j,3)
minset = float("inf")
for ele in first:
    for eles in second:
        temp = abs(eles[0]-ele[0])+abs(eles[1]-ele[1])
        if temp<minset:
            minset = temp
print(minset-1)



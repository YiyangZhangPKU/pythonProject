import bisect
n = int(input())
numlist = list(map(int,input().split()))
numlist.sort()
numtree = [[i,[],[]]for i in numlist]
heightcount = []
def totalvalue(tree,height):
    if tree[1] == [] and tree[2] == []:
        heightcount.append((tree[0],height))
    else:
        totalvalue(tree[1],height+1)
        totalvalue(tree[2],height+1)

while len(numtree) >1:
    left = numtree.pop(0)
    right = numtree.pop(0)
    numlist.pop(0)
    numlist.pop(0)
    intend = [left[0]+right[0],left,right]
    a = bisect.bisect_left(numlist,intend[0])
    numlist.insert(a,intend[0])
    numtree.insert(a,intend)
numtree = numtree[0]
totalvalue(numtree,0)
count = 0
for ele in heightcount:
    count+=ele[0]*ele[1]
print(count)


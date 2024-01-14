n,m = map(int,input().split())
budgetlist = []
for i in range(n):
    budgetlist.append(int(input()))

def ispossible(maxbud):
    currentcost = 0
    divideround = 1
    for i in range(n):
        if budgetlist[i] > maxbud:
            return 0
        if currentcost+budgetlist[i] > maxbud:
            divideround += 1
            currentcost = budgetlist[i]
        else:
            currentcost+=budgetlist[i]
    if divideround > m:
        return 0
    else:
        return 1

def bifind(left,right):
    if left == right:
        return left
    if right == left+1:
        if ispossible(left):
            return left
        else:
            return right
    mid = ((left+right)>>1)
    if ispossible(mid):
        return bifind(left,mid)
    else:
        return bifind(mid,right)

small = max(budgetlist)
big = sum(budgetlist)

print(bifind(small,big))


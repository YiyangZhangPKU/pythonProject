n = int(input())
numlist = list(map(int,input().split()))
target = int(input())
numlist.sort()
flag = 0
bigindex = n-1
for i in range(n):
    if numlist[i] > target:
        break
    small = numlist[i]
    if i >= bigindex:
        break
    if small + numlist[bigindex] == target:
        print(small, numlist[bigindex])
        flag = 1
        break
    while (small +numlist[bigindex] > target) and (bigindex >i+1):
        if small +numlist[bigindex-1] > target:
            bigindex -= 1
            continue
        elif small +numlist[bigindex-1] == target:
            print(small,numlist[bigindex-1])
            flag = 1
            break
        else:
            bigindex -= 1
            break
    if flag == 1:
        break
if flag == 0:
    print("No")


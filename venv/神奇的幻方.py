n = int(input())
outlist = [[0 for i in range(2*n-1)]for j in range(2*n-1)]
row = 0
col = n-1
for i in range(1,(2*n-1)*(2*n-1)+1):
    outlist[row][col] = i
    if row == 0 and col == 2*n-2:
        row = 1
    elif outlist[(row-1)%(2*n-1)][(col+1)%(2*n-1)] != 0:
        row += 1
    else:
        row = (row-1)%(2*n-1)
        col = (col+1)%(2*n-1)
for i in range(2*n-1):
    print(*outlist[i])


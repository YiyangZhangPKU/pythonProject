col = int(input())
wordlist = input()
row = len(wordlist)//col
solvematrix = []
addsum = 0
for i in range(row):
    addsum += 1
    sign = -1 if addsum%2 == 0 else 1
    if sign == 1:
        temp = list(wordlist[col*addsum-col:col*addsum])
    else:
        temp = list(wordlist[col*addsum-1:col*addsum-col-1:-1])
    solvematrix.append(temp)
output = []
for i in range(col):
    for j in range(row):
        output.append(solvematrix[j][i])
print("".join(output))

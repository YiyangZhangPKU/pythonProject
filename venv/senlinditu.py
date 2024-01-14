n = int(input())
martrix = []
dicall = {}
for i in range(n):
    temp = list(input())
    martrix.append(temp)
    for item in temp:
        if item == " ":
            continue
        if item not in dicall:
            dicall[item] = 1
        else:
            dicall[item] += 1
sub = list(dicall.items())
sub.sort(key = lambda x:(-x[1],x[0]))
max = []
maxi = sub[0][1]
for item in sub:
    if item[1] == maxi:
        max.append(item[0])
    else:
        break
print(*max)
for i in range(n):
    for j in range(n):
        if martrix[i][j] == " ":
            continue
        elif martrix[i][j] in max:
            martrix[i][j] = "*"
        else:
            martrix[i][j]= "."
for k in range(n):
    print(*(martrix[k]),sep="")






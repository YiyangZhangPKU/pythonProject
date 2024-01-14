wordlist = input()
highest = 0
sep = []
temp =[]
tag = 0
for i in range(len(wordlist)):
    if wordlist[i]!="+":
        tag = i
        temp.append(wordlist[i])
    else:
        sep.append(temp)
        temp = []
sep.append(temp)

for i in range(len(sep)):
    if sep[i][0] == "0":
        continue
    for j in range(len(sep[i])):
        if sep[i][j] == "^":
            hight = int("".join(sep[i][j+1:]))
            if hight > highest:
                highest = hight
            break

print(f"n^{highest}")



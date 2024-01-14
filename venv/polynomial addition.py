n = int(input())
for i in range(n):
    outcutlist1 = list(map(int,input().split()))
    outcutlist2 = list(map(int,input().split()))
    outdict = {}
    for j in range(0,len(outcutlist1)-2,2):
        if outcutlist1[j + 1] in outdict:
            outdict[outcutlist1[j + 1]] += outcutlist1[j]
        else:
            outdict[outcutlist1[j + 1]] = outcutlist1[j]
    for j in range(0,len(outcutlist2)-2,2):
        if outcutlist2[j+1] in outdict:
            outdict[outcutlist2[j+1]] += outcutlist2[j]
        else:
            outdict[outcutlist2[j + 1]] = outcutlist2[j]
    outmap = list(outdict.items())
    outmap.sort(key = lambda x:-x[0])
    outdust = []
    for j in range(len(outmap)):
        if outmap[j][1] != 0:
            outdust.append(f"[ {outmap[j][1]} {outmap[j][0]} ]")
    if outdust == []:
        print()
        continue
    print(*outdust)
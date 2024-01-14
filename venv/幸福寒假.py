n = int(input())
planlist =[]
for i in range(n):
    begindate,enddate,value = input().split()
    firstpart,secondpart = begindate.split(".")
    if firstpart == "1":
        begindate = int(secondpart)-7
    else:
        begindate = 31+int(secondpart)-7
    firstpart,secondpart = enddate.split(".")
    if firstpart == "1":
        enddate = int(secondpart)-7
    else:
        enddate = 31+int(secondpart)-7
    if enddate>51-7:
        continue
    value = int(value)
    planlist.append((begindate,enddate,value))
planlist.sort(key=lambda x:x[1])
conp = [0]
dp = [0 for i in range(len(planlist)+1)]
for i in range(1,len(planlist)):
    count = 0
    for j in range(0,i):
        if planlist[j][1]<planlist[i][0]:
            count+=1
    conp.append(count)
flag = 0
for i in range(1,len(planlist)+1):
    if i==2:
        dp[i] = planlist[i][2]
    dp[i] = max(dp[conp[i-1]]+planlist[i-1][2],dp[i-1])

print(dp[-1])



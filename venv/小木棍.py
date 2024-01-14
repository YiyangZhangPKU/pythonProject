def dfs(section,currentlength,beginindex):
    if section == toalsection:
        return True
    if currentlength == i:
        return dfs(section+1,0,0)
    flag = 0
    for j in range(beginindex,n):
        if not used[j] and flag != num[j] and currentlength+num[j]<= i:
            used[j] = 1
            if dfs(section,currentlength+num[j],j+1):
                return True
            else:
                flag = num[j]
                used[j] = 0
                if currentlength == 0 :
                    return False

while True:
    n = int(input())
    if n == 0:
        break
    num = list(map(int,input().split()))
    num.sort(reverse=True)
    Highest = sum(num)
    Least = max(num)
    for i in range(Least,Highest//2+1):
        if Highest%i:
            continue
        else:
            toalsection = Highest//i
            used = [0 for i in range(n)]
            keyflag = dfs(1,0,0)
            if keyflag:
                print(i)
                break
            else:
                continue
    if not keyflag:
        print(Highest)


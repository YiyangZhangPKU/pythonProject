line1 = input()
line2 = input()
dp = [[0 for i in range(len(line2)+1)]for j in range(len(line1)+1)]
for i in range(len(line1)+1):
    for j in range(len(line2)+1):
        if i == 0 or j == 0:
            dp[i][j] = 0
            continue
        if line2[j-1] == line1[i-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])


print(dp[len(line1)][len(line2)])


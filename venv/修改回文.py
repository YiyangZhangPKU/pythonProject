line = input()
n = len(line)
if line == line[::-1]:
    print(0)
    exit(0)
dp = [[0 for i in range(n)]for j in range(n)]

for i in range(n-1,-1,-1):
    for j in range(i+1,n):
        if i != j:
            qa = dp[i][j-1]+1
            qb = dp[i+1][j] +1
            qc = dp[i+1][j-1] if line[i] == line[j] else dp[i+1][j-1]+1
            dp[i][j] = min(qa,qb,qc)

print(dp[0][n-1])


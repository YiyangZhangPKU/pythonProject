t,m=map(int,input().split())
value=[]
time=[]
for i in range(m):
    t,v=map(int,input().split())
    value.append(v)
    time.append(t)
dp = [[ 0 for j in range(t+2)] for i in range(m+2)]
for i in range(1,m+1):
    for j in range(1,t+1):
        if j-time[i]>=0:
           dp[i][j]=max(dp[i-1][j],dp[i-1][j-time[i]]+value[i])
        else:
            dp[i][j]=dp[i-1][j]
print(dp[m][t])
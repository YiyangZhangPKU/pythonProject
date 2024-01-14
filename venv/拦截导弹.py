num = int(input())
missile =list(map(int, input().split()))
dp = [1 for i in range(num)]
for i in range(num-2,-1,-1):
    temp = 1
    for j in range(i+1,num):
        if missile[j] > missile[i]:
            continue
        else:
            temp = dp[j]+1 if dp[j]+1 > temp else temp
    dp[i] = temp

print(max(dp))




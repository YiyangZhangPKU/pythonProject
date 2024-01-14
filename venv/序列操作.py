n,m = map(int,input().split())
k = m%n
listnum = list(map(int,input().split()))
listnum1 = listnum[k:]+listnum[0:k]
print(*listnum1)
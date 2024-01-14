numlist = list(map(int,input().split()))
even = []
odd = []
for ele in numlist:
    if ele%2:
        odd.append(ele)
    else:
        even.append(ele)
odd.sort(reverse=True)
even.sort()
print(*odd,*even)
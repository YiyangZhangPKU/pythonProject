r = int(input())
n = int(input())
sum_of_area = [0 for i in range(r+1)]
for i in range(n):
    X,Y,Width,Height = map(int,input().split())
    for j in range(X+1,X+Width+1):
        sum_of_area[j]+=Height
toatlarea = sum(sum_of_area)
sumpart = 0
for i in range(r+1):
    sumpart+=sum_of_area[i]
    if sumpart*2>=toatlarea:
        break
for j in range(i+1,r+1):
    if sum_of_area[j] == 0:
        i+=1
    else:
        break
print(i)


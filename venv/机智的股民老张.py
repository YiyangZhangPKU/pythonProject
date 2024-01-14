def max_sub_cross(lista,low,high,mid):
    leftmax = -1000000000000
    sumlist = 0
    for i in range(mid,low-1,-1):
        sumlist += lista[i]
        if sumlist > leftmax:
            leftmax = sumlist
            lefttag =i
 #           print(lefttag)
    rightmax = -1000000000000
    sumlist = 0
    for i in range(mid+1,high+1):
        sumlist += lista[i]
        if sumlist > rightmax:
            rightmax = sumlist
            righttag =i
 #           print(righttag)
#    print(lefttag,righttag,leftmax+rightmax,mid,leftmax,rightmax)
    return (lefttag,righttag,leftmax+rightmax)

def max_sub(lista,low,high):
    if low == high:
        return (low,high,lista[low])
    else:
        mid = (low+high)//2
        leftlow,lefthigh,leftsum = max_sub(lista,low,mid)
        rightlow,righthigh,rightsum = max_sub(lista,mid+1,high)
        crosslow,crosshigh,crosssum = max_sub_cross(lista,low,high,mid)

        if leftsum>=rightsum and leftsum>=crosssum:
            return (leftlow,lefthigh,leftsum)
        elif rightsum>=leftsum and rightsum>=crosssum:
            return (rightlow,righthigh,rightsum)
        else:
            return (crosslow,crosshigh,crosssum)


numlist = list(map(int,input().split()))
changelist = [numlist[i+1]-numlist[i] for i in range(len(numlist)-1)]
profita = max_sub(changelist,0,len(changelist)-1)[2]
if profita > 0:
    print(profita)
else:
    print(0)





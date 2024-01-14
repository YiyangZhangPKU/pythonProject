def ispre(str1:str,str2:str):
    if len(str1) >len(str2):
        return False
    elif len(str1) <len(str2):
        if str1 == str2[:len(str1)]:
            return True
        else:
            return False
    else:
        if str1 == str2:
            return True
        else:
            return False

T = int(input())
for _ in range(T):
    n = int(input())
    telephone = []
    for i in range(n):
        telephone.append(input())
    telephone.sort()
    flag = 0
    for i in range(n-1):
        if ispre(telephone[i],telephone[i+1]):
            flag = 1
            break
    if flag == 1:
        print("NO")
    else:
        print("YES")


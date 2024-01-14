s = list(input())
num = 0
sign = 0
for item in s:
    if item == "(":
        num += 1
    else:
        num -= 1
    if num == 0:
        sign+=1
print(sign)

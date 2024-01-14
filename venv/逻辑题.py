alllist = []
for i in range(0,1024):
	alllist.append(str(bin(i)[2:]).zfill(10))

def eq(ql):
    a = 0
    b = 0
    for i in ql:
        if i == "0":
            a+=1
        else:
            b+=1
    if a == b:
        return True
    else:
        return False


def Q3(ql):
    return ~ (int(ql[2])^("00" in ql))

def Q4(ql):
    return ~ (int(ql[3])^(ql[3] != ql[7]))

def Q5(ql):
    return ~ (int(ql[4])^(ql[6] != ql[8]))

def Q6(ql):
    return ~ (int(ql[5])^(eq(ql)))

def Q8(ql):
    return ~ (int(ql[7])^("111" in ql))

def Q9(ql):
    return ~ (int(ql[8])^(ql[3]==ql[4]))

def Q10(ql):
    return ~ (int(ql[9])^(ql[5]==ql[7]))

for element in alllist:
    if (element[0] == "1") and (element[1] == "1") and (element[6] == "0"):
        if Q3(element) and Q4(element) and Q5(element) and Q6(element) and Q8(element) and Q9(element) and Q10(element):
            print(element)

##这个代码有问题
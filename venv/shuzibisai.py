miao = list(input().split())
yan = list(input().split())
maxlength = 0
for i in range(len(miao)):
    maxlength = len(miao[i]) if len(miao[i]) > maxlength else maxlength
for i in range(len(miao)):
    if miao[i] == "0":
        miao[i] = ((0,1))
    else:
        t= len(miao[i])
        miao[i] = (int(miao[i]+("9"*(maxlength-t))),t)
maxlength = 0
for i in range(len(yan)):
    maxlength = len(yan[i]) if len(yan[i]) > maxlength else maxlength
for i in range(len(yan)):
    if yan[i] == "0":
        yan[i] = (0,1)
    else:
        t= len(yan[i])
        yan[i] = (int(yan[i] + ("9" * (maxlength - t))), t)

miao.sort(key=lambda x:-x[0])
yan.sort(key=lambda x: -x[0])
for i in range(len(miao)):
    miao[i] = str(miao[i][0])[:miao[i][1]]
for i in range(len(yan)):
    yan[i] = str(yan[i][0])[:yan[i][1]]
#print(yan,miao)
miaoall = int("".join(miao))
yanall = int("".join(yan))
if miaoall == yanall:
    print("Same")
elif miaoall < yanall:
    print("Yan")
else:
    print("Miao")
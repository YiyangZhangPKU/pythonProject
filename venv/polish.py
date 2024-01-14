inputlist = list(input().split())
operator = ["+","-","*","/"]
outlist = []
for ele in inputlist:
    if ele not in operator:
        outlist.append(float(ele))
    else:
        outlist.append(ele)
operatorstack = []

def calculate(op,op2,op1):
    """计算辅助函数"""
    if op == "*":
        return op1*op2
    elif op =="/":
        return op2/op1
    elif op == "+":
        return op1+op2
    else:
        return op2-op1

for i in range(len(inputlist)-1,-1,-1):

    if outlist[i] not in operator:
        operatorstack.append(outlist[i])
    else:
        second = operatorstack.pop()
        first = operatorstack.pop()

        operatorstack.append(calculate(outlist[i],second,first))
print("%2f"  %operatorstack[0])
def RevesePolishTransform(lista):
    """合理的中缀式转化为后缀式"""
    prec= {"*":3,"/":3,"+":2,"-":2,"(":1}
    opstack = []
    outputlist = []
    for ele in lista:
        if ele not in prec and ele != "(" and ele != ")":
            outputlist.append(ele)
        elif ele == "(":
            opstack.append(ele)
        elif ele == ")":
            while opstack[-1] != "(":
                outputlist.append(opstack.pop())
            else:
                opstack.pop()
        else:
            while len(opstack) > 0 and (prec[opstack[-1]]>=prec[ele]):
                outputlist.append(opstack.pop())
            opstack.append(ele)
    while len(opstack) > 0:
        outputlist.append(opstack.pop())
    return outputlist

def calculate(op,op2,op1):
    """计算辅助函数"""
    if op == "*":
        return op1*op2
    elif op =="/":
        return op1/op2
    elif op == "+":
        return op1+op2
    else:
        return op1-op2

def ReversePolishCalulate(expr):
    """后缀式的计算"""
    opreadstack = []
    prec = {"*": 3, "/": 3, "+": 2, "-": 2}
    for ele in expr:
        if ele not in prec:
            opreadstack.append(ele)
        else:
            op2 = opreadstack.pop()
            op1 = opreadstack.pop()
            opreadstack.append(calculate(ele,op2,op1))
    if len(opreadstack) == 1:
        return opreadstack[0]
    else:
        return "sign"

def brackettest(lista):
    """测试括号匹配和括号里有没有式子"""
    spcount = 0
    i = 0
    baccount = 0
    emptytest = 0
    for ele in lista:
        i += 1
        if ele == "(":
            baccount += 1
            spcount = i
        if ele == ")":
            baccount -= 1
            if baccount < 0:
                return 0
            if i == spcount + 1:
                emptytest = 1    #空表达式
        if baccount < 0:
            return 0
    if baccount :
        return 0    #不匹配
    elif emptytest:
        return 2
    else:
        return 1  #匹配且非空

vaild = ["+","-","*","/","."," ","(",")"]+[str(x) for x in range(10)]
num = [str(x) for x in range(10)]
while True:
    expressionor = input()
    expression = []
    for ele in expressionor:
        if ele != " ":
           expression.append(ele)
    expression = "".join(expression)
    if not expression:
        print("No expression.")
        continue
    if expression == "quit":
        break
    cut = []
    flag = 1
    specialtrnsformflag = 0
    temp = []
    for i in range(len(expression)):
        if expression[i] not in vaild:
            print("Unknown operator.")
            flag =0
            break
        if expression[i] != "."and expression[i] not in num and temp:
            if specialtrnsformflag == 1:
                cut.append(float("".join(temp)))
                temp = []
                cut.append(")")
                specialtrnsformflag = 0
            else:
                cut.append(float("".join(temp)))
                temp = []
        if expression[i] == "(" or expression[i] == ")":
            cut.append(expression[i])
        if (expression[i] == "+" or expression[i] == "-"):
            if  i == len(expression)-1 :
                flag = 0
                print("Not implemented.")
                break
            if (not cut) or ((not isinstance(cut[-1],float)) and cut[-1] != ")"):
                if(expression[i+1] not in num and (expression[i+1] != "(")): #加减法前后都不是数字
                    flag = 0
                    print("Not implemented.")
                    break
                else:                                                   #后面是数字，前面不是，当单目处理,需要一个flag加括号
                    cut.append("(")
                    cut.append(0)
                    cut.append(expression[i])
                    specialtrnsformflag = 1
            else:
                if expression[i+1] == ")":
                    flag = 0
                    print("Not implemented.")
                    break
                cut.append(expression[i])
        if (expression[i] == "*" or expression[i] == "/"):
            if (not cut) or ((not isinstance(cut[-1],float) and cut[-1] != ")")):
                flag = 0            #乘除法前面必须是数字
                print("Not implemented.")
                break
            elif i+1 == len(expression) or( expression[i+1] == ")"):
                flag = 0
                print("Not implemented.")
                break
            else:
                cut.append(expression[i])
        if (expression[i] == "."):
            if  i == len(expression)-1 :
                flag = 0
                print("Not implemented.")
                break
            if "." in temp:
                flag = 0
                print("Not implemented.")
                break
            if ((not temp) or (temp[-1] not in num))or expression[i+1] not in num:
                flag = 0            #dot前后必须是数字
                print("Not implemented.")
                break
            else:
                temp.append(expression[i])
        if expression[i] in num:            #数字的处理
            temp.append(expression[i])

    if flag == 0:
        continue
    if  temp:
        cut.append(float("".join(temp)))
    if specialtrnsformflag == 1:
        cut.append(")")
    testlineforbac = brackettest(cut)
    if testlineforbac == 0:
        print("Unmatched bracket.")
        continue
    elif testlineforbac == 2:
        print("No expression.")
        continue
    else:
        output = ReversePolishCalulate(RevesePolishTransform(cut))
        if output == "sign":
            print("Not implemented.")
            continue
        print("%.3f"  %output)


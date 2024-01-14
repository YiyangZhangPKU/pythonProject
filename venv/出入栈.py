origianlc = list(input())
word = {}
for i in range(len(origianlc)):
    word[origianlc[i]] = i
while True:
    try:
        origianl = origianlc.copy()
        test = input()
        if len(test) != len(origianl):
            print("NO")
        else:
            pointercount = 0
            testlist = []
            for j in range(len(test)):
                if test[j] not in word:
                    testlist.append(0)
                    break
                if word[test[j]] >= pointercount:
                    while origianl and word[origianl[0]] <= word[test[j]]:
                        testlist.append(origianl.pop(0))
                        pointercount = word[test[j]]
                if word[test[j]] == pointercount:
                    testlist.pop()
                    pointercount  =word[testlist[-1]] if testlist else 0
                if word[test[j]] < pointercount:
                    break
            if not testlist:
                print("YES")
            else:
                print("NO")
    except EOFError:
        break





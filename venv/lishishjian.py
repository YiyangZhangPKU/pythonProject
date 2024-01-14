n = int(input())
History = []
for i in range(n):
    name,begin,end = input().split()
    History.append((name,int(begin),int(end)))
while True:
    try:
        request = input()
        try:
            request = int(request)
            listname = []
            for item in History:
                if item[1] <= request and request <= item[2]:
                    listname.append(item[0])
            listname.sort()
            print(*listname)
        except:
            for item in History:
                if item[0] == request:
                    print(item[1],end = " ")
                    print(item[2])
    except EOFError:
        break



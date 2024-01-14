class Tree:
    def __init__(self,root,childnodeList):
        self.key = root
        self.child = childnodeList
        self.danger = 0
    def isLeaf(self):
        return self.child == {}
T = int(input())
for _ in range(T):
    flag = 0
    n = int(input())
    classTree = Tree(0,{})
    for i in range(n):
        if flag == 1:
            continue
        telephone = list(map(int,list(input())))
        currentNode = classTree
        if i == 0:
            for ele in telephone:
                currentNodeTemp = Tree(ele,{})
                currentNode.child[ele] = currentNodeTemp
                currentNode = currentNodeTemp
            currentNode.danger = 1
        else:
            for ele in telephone:
                if ele in currentNode.child:
                    currentNode = currentNode.child[ele]
                    continue
                if currentNode.danger == 1:
                    flag = 1
                    break
                currentNodeTemp = Tree(ele,{})
                currentNode.child[ele] = currentNodeTemp
                currentNode = currentNodeTemp
                if flag == 1:
                    continue
            currentNode.danger = 1

    if flag:
        print("NO")
    else:
        print("YES")











class Tree:
    def __init__(self,root,nodeList,parent = None,height = 0):
        self.key = root
        self.child = nodeList
        self.parent = parent
        self.height = height
    def addChild(self,key):
        temp = Tree(key, [], parent=self,height = self.height+1)
        self.child.append(temp)
        return temp
    def isLeaf(self):
        return self.child == []
def dfs(tree:Tree):
    if tree.height !=0:
        if tree.isLeaf():
            print(" "*(tree.height-1),end="")
            print(tree.key)
        else:
            print(" " * (tree.height - 1), end="")
            print(tree.key)
            for member in tree.child:
                dfs(member)
    else:
        for member in tree.child:
            dfs(member)
def sortTree(tree:Tree):
    if tree.isLeaf():
        return
    else:
        tree.child.sort(key = lambda x:x.key)
        for member in tree.child:
            sortTree(member)

n= int(input())
directory = Tree(0,[])
for _ in range(n):
    optionlist = list(input().split("\\"))
    currentNode = directory
    for ele in optionlist:
        flag = 0
        for child in currentNode.child:
            if child.key == ele:
                currentNode = child
                flag = 1
                break
        if flag == 1:
            continue

        currentNode = currentNode.addChild(ele)
sortTree(directory)
dfs(directory)




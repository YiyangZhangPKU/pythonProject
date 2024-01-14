class BinaryTree(object):
    def __init__(self, rootObj, left=None, right=None):
        self.key = rootObj
        self.leftChild = left
        self.rightChild = right

    def insertLeft(self, newNode):
        self.leftChild = BinaryTree(newNode, left=self.leftChild)

    def insertRight(self, newNode):
        self.rightChild = BinaryTree(newNode, right=self.rightChild)

class Tree:
    def __init__(self,root,nodeList = []):
        self.key = root
        self.child = nodeList
    def addChild(self,key):
        self.child.append(Tree(key,[]))
def BinaryHeight(tree:BinaryTree):
    if tree.leftChild == None and tree.rightChild == None:
        return 1
    elif tree.leftChild == None:
        return BinaryHeight(tree.rightChild)+1
    elif tree.rightChild == None:
        return BinaryHeight(tree.leftChild)+1
    else:
        return max(BinaryHeight(tree.leftChild)+1,BinaryHeight(tree.rightChild)+1)
dfsdata = input()
originalTree = Tree(0)
Nodestack = []
temp =0
originalheight = 0
nodecount =0
curr = originalTree
for ele in dfsdata:
    if ele == "d":
        Nodestack.append(curr)
        temp+=1
        nodecount += 1
        originalheight = temp if temp>originalheight else originalheight
        curr.addChild(nodecount)
        curr = (curr.child)[-1]
    else:
        curr = Nodestack.pop()
        temp-=1
convertTree = BinaryTree(0)
def TreeConvert(orinode:Tree,binode:BinaryTree):
    curr = binode
    binode.key = orinode.key
    for i in range(len(orinode.child)):
        ele = orinode.child[i]
        if not i :
            curr.insertLeft(ele.key)
            curr = curr.leftChild
            if ele.child != []:
                TreeConvert(ele,curr)
        else:
            curr.insertRight(ele.key)
            curr = curr.rightChild
            if ele.child != []:
                TreeConvert(ele,curr)

TreeConvert(originalTree,convertTree)
afterheight = BinaryHeight(convertTree)-1
print("%d => %d" %(originalheight,afterheight))










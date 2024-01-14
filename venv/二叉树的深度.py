class BinaryTree(object):
    def __init__(self, rootObj, left=None, right=None):
        self.key = rootObj
        self.leftChild = left
        self.rightChild = right

    def insertLeft(self, newNode):
        self.leftChild = BinaryTree(newNode, left=self.leftChild)

    def insertRight(self, newNode):
        self.leftChild = BinaryTree(newNode, right=self.rightChild)
def BinaryHeight(tree:BinaryTree):
    if tree.leftChild == None and tree.rightChild == None:
        return 1
    elif tree.leftChild == None:
        return BinaryHeight(tree.rightChild)+1
    elif tree.rightChild == None:
        return BinaryHeight(tree.leftChild)+1
    else:
        return max(BinaryHeight(tree.leftChild)+1,BinaryHeight(tree.rightChild)+1)

n = int(input())
Nodedict = {i:BinaryTree(i) for i in range(1,n+1)}
for i in range(n):
    left,right = map(int,input().split())
    if left!= -1:
        Nodedict[i + 1].leftChild = Nodedict[left]
    if right!= -1:
        Nodedict[i+1].rightChild = Nodedict[right]
print(BinaryHeight(Nodedict[1]))


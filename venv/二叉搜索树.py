class TreeNode:
    def __init__(self,key,val,left = None,right = None,parent = None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
    def hasLeftChild(self):
        return self.leftChild
    def hasRightChild(self):
        return self.rightChild
    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self
    def isRightChild(self):
        return self.parent and self.parent.rightChild == self
    def isRoot(self):
        return not self.parent
    def isLesf(self):
        return not(self.leftChild or self.rightChild)
    def hasAnyChildren(self):
        return self.rightChild or self.leftChild
    def hasBothChildren(self):
        return self.leftChild and self.rightChild
    def repalceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0
    def length(self):
        return self.size
    def __len__(self):
        return self.size
    def __iter__(self):
        return self.root.__iter__()
    def put(self,key,val = 0):
        if self.root:
            self.size+=self._put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)
            self.size = 1
    def _put(self,key,val,currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                return self._put(key,val,currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key,val,parent=currentNode)
                return 1
        elif key >currentNode.key:
            if currentNode.hasRightChild():
                return self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)
                return 1
        else:
            currentNode.payload = val
            return 0




k = []
def postOrder(tree):
    if tree:
        k.append(tree.key)
        postOrder(tree.leftChild)
        postOrder(tree.rightChild)

searchlist = list(map(int,input().split()))
a = BinarySearchTree()
for ele in searchlist:
    a.put(ele,ele)
postOrder(a.root)
print(*k)


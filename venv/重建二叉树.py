class BinaryTree(object):
    def __init__(self, rootObj, left=None, right=None):
        self.key = rootObj
        self.leftChild = left
        self.rightChild = right

    def insertLeft(self, newNode):
        self.leftChild = BinaryTree(newNode, left=self.leftChild)

    def insertRight(self, newNode):
        self.leftChild = BinaryTree(newNode, right=self.rightChild)

def Reconstruct(preorder,inorder,rootNode):
    root = preorder[0]
    rootNode.key = root
    rootNode.leftChild = BinaryTree(None)
    rootNode.rightChild = BinaryTree(None)
    lf = 1
    rf = 1
    dividetag = inorder.index(root)
    inleft = inorder[0:dividetag]
    inright = inorder[dividetag+1:]
    preleft = preorder[1:1+dividetag]
    preright = preorder[1+dividetag:]
    leftnode = rootNode.leftChild
    rightnode = rootNode.rightChild
    if not inleft:
        rootNode.leftChild = None
        lf = 0
    if not inright:
        rootNode.rightChild = None
        rf = 0
    if lf:
        Reconstruct(preleft,inleft,leftnode)
    if rf:
        Reconstruct(preright,inright,rightnode)

def postOrder(tree:BinaryTree):
    if tree:
        postOrder(tree.leftChild)
        postOrder(tree.rightChild)
        postorder.append(tree.key)
while True:
    try:
        preorder,inorder = input().split()
        outTree = BinaryTree(None)
        Reconstruct(preorder,inorder,outTree)
        postorder = []
        postOrder(outTree)
        print("".join(postorder))
    except:
        break
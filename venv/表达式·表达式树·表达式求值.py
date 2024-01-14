class BinaryTree(object):
    def __init__(self, rootObj, left=None, right=None):
        self.key = rootObj
        self.leftChild = left
        self.rightChild = right

    def insertLeft(self, newNode):
        self.leftChild = BinaryTree(newNode, left=self.leftChild)

    def insertRight(self, newNode):
        self.leftChild = BinaryTree(newNode, right=self.rightChild)


expression = input()
n = int(input())
alphadict = {}
for i in range(n):
    letter,value = input().split()
    alphadict[letter]=int(value)


class BinHeap:
    def __init__(self):
        self.heaplist = [0]
        self.currentSize = 0

    def precUp(self,i):
        while i//2 > 0:
            if self.heaplist[i] > self.heaplist[i//2]:
                self.heaplist[i],self.heaplist[i//2] = self.heaplist[i//2],self.heaplist[i]
                i = i//2
            else:
                break
    def maxChild(self,i):
        if i*2+1 >self.currentSize:
            return i*2
        else:
            if self.heaplist[i*2] > self.heaplist[i*2+1]:
                return i*2
            else:
                return i*2+1

    def precDown(self,i):
        while (i*2)<= self.currentSize:
            mc = self.maxChild(i)
            if self.heaplist[i] <self.heaplist[mc]:
                self.heaplist[i],self.heaplist[mc] = self.heaplist[mc],self.heaplist[i]
            i = mc
    def insert(self,k):
        self.heaplist.append(k)
        self.currentSize += 1
        self.precUp(self.currentSize)
    def delMax(self):
        retval = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.currentSize]
        self.currentSize -= 1
        self.heaplist.pop()
        self.precDown(1)
        return retval
    def findMax(self):
        return self.heaplist[1]
    def buildHeap(self,alist):
        i = len(alist)//2
        self.currentSize = len(alist)
        self.heaplist = [0]+alist[:]
        while(i>0):
            self.precDown(i)
            i -= 1



T = int(input())
for _ in range(T):
    m,n = map(int,input().split())
    numbermatrix= []
    for i in range(m):
        numbermatrix.append(sorted(list(map(int,input().split()))))
    templist = numbermatrix[0]

    for i in range(m-1):
        newHeap = BinHeap()
        templistA = [templist[j]+numbermatrix[i+1][0] for j in range(n)]
        newHeap.buildHeap(templistA)
        for j in numbermatrix[i+1][1:]:
            for k in templist:
                if j+k > newHeap.findMax():
                    break
                else:
                    newHeap.delMax()
                    newHeap.insert(j+k)
        templist = []
        for j in range(n):
            templist.append(newHeap.delMax())
        templist.reverse()
    print(*templist)










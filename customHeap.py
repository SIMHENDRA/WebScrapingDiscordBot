from math import floor
class objHeap:

    def __init__(self, label, isMaxHeap):
        self.H = [] 
        self.cat = label
        self.dir = isMaxHeap
        self.size = 0

    def priocomp(self, A, B): #returns true if A has higher priority than B, False if lower or equal priority to B
        if dir:
            if A[self.cat] > B[self.cat]:
                return True
            else:
                return False
        else:
            if A[self.cat] < B[self.cat]:
                return True
            else:
                return False

    def isLeaf(self, ind):
        if 2*ind > (self.size-1):
            return True
        else:
            return False
    
    def getPar(self, ind):
        return floor(ind/2)

    def getL(self, ind):
        if 2*ind + 1 <= self.size-1:
            return 2*ind + 1
        else:
            return -1

    def getR(self, ind):
        if 2*ind + 2 <= self.size-1:
            return 2*ind + 2
        else:
            return -1
    
    def swap(self, indA, indB):
        temp = self.H[indA]
        self.H[indA] = self.H[indB]
        self.H[indB] = temp
        return

    def push(self, plane):
        self.size += 1
        self.H.append(plane)
        ind = self.size-1
        while (ind != 0):
            par = self.getPar(ind)
            if self.priocomp(plane, self.H[par]):
                self.swap(ind, par)
                ind = par
            else:
                break

    def adj(self, ind):
        if isLeaf(ind):
            return
        r = self.getR(ind)
        m = self.getL(ind)
        if r == -1:
            if self.priocomp(self.H[m], self.H[ind]):
                self.swap(m, ind)
                self.adj(m)
            return
        else:
            if self.priocomp(self.H[m], self.H[r]):
                if self.priocomp(self.H[m], self.H[ind]):
                    self.swap(m, ind)
                    self.adj(m)
            else:
                if self.priocomp(self.H[r], self.H[ind]):
                    self.swap(r, ind)
                    self.adj(r)
            return

    def pop(self):
        self.size -= 1
        ret = self.H[0]
        self.H[0] = self.H[self.size-1]
        self.adj(0)
        return ret

        
    
        


    

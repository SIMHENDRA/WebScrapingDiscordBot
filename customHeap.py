from math import floor
class objHeap:

    def __init__(self, label, isMaxHeap):
        self.H = [] 
        self.cat = label
        self.dir = isMaxHeap
        self.size = 0

    def compare(self, A, B): #returns true if A has higher priority than B, False if lower or equal priority to B
        if dir:
            if A[cat] > B[cat]:
                return True
            else:
                return False
        else:
            if A[cat] < B[cat]:
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
            par = getPar(ind)
            if compare(plane, self.H(par)):
                swap(ind, par)
                ind = par
            else:
                break
    def adj(self, ind):
        if isLeaf(ind):
            return
        r = getR(ind)
        m = getL(ind)
        if r == -1:
            if compare(self.H[m], self.H[ind]):
                swap(m, ind)
                adj(m)
            return
        else:
            if compare(self.H[m], self.H[r]):
                if compare(self.H[m], self.H[ind]):
                    swap(m, ind)
                    adj(m)
            else:
                if compare(self.H[r], self.H[ind]):
                    swap(r, ind)
                    adj(r)
            return

    def pop(self):
        self.size -= 1
        ret = self.H[0]
        self.H[0] = self.H[size-1]
        adj(0)
        return ret

        
    
        


    

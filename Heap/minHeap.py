from heapq import heappush,heappop,heapify


class MinHEAP:
    def __init__(self):
        self.heap=[]
    def parent(self,i):
        return (i-1/2)
    def insertKey(self,k):
       heappush(self.heap,k)
    
    def decreaseKey(self,index,newValue):
        self.heap[index]=newValue
        while(index != 0 and self.heap[self.parent(index)] > self.heap[index]):
            self.heap[index] , self.heap[self.parent(index)] = (self.heap[self.parent(index)], self.heap[index])

    def extract(self):
        return heappop(self.heap)

    def deleteKey(self,i):
        self.decreaseKey(i, -1)
        self.extract()

    def insert(self,value):
        self.heap.append(value)
        # iterate to check each value to be bigger than root
        # while(self.heap[self.parent]> self.heap[len(self.heap)-1]):

    def delete(self,key):
        minimum = self.heap[0]
        self.heap[0] =self.heap[len(self.heap.length) -1]
        self.heap.pop()
        # iteration and check sort values  


heapObj = MinHEAP()
heapObj.insertKey(3)
heapObj.insertKey(2)
heapObj.deleteKey(1)
heapObj.insertKey(15)
heapObj.insertKey(5)
heapObj.insertKey(4)
heapObj.insertKey(45)
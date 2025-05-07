class MaxHeap:
    def __init__(self):
        self.heap=[]

    def insert(self,value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1) 

    def deletion(self):
        max_value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
 

        self.heapify_down(0)
        return max_value

    def heapify_up(self,index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] >  self.heap[parent]:
            self.heap[index] , self.heap[parent] = self.heap[parent] , self.heap[index] 
            self.heapify_up(parent)

    def heapify_down(self,index):
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index 

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        

        if largest != index:
            self.heap[index] , self.heap[largest] = self.heap[largest] , self.heap[index]
            self.heapify_down(largest)
    
    def display(self):
        print('Max-heap',self.heap)









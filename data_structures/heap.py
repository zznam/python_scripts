class MinInHeap:
    def __init__(self) -> None:
        self.size = 0
        self.items = []
        self.size = 7
        self.items = [10, 15, 20, 17, 25, 21, 24]
        pass

    def getLeftChildIndex(self, parentIndex):
        return (parentIndex << 1) + 1

    def getRightChildIndex(self, parentIndex):
        return (parentIndex << 1) + 2

    def getParentIndex(self, index):
        if index >= self.size: return None
        if index == 0: return None
        return ((index - 1) >> 1)

    def hasLeftChild(self, index):
        return self.getLeftChildIndex(index) < self.size

    def hasRightChild(self, index):
        return self.getRightChildIndex(index) < self.size

    def hasParent(self, index):
        return self.getParentIndex(index) != None

    def leftChild(self, index):
        if self.hasLeftChild(index):
            return self.items[self.getLeftChildIndex(index)]
        return None

    def rightChild(self, index):
        if self.hasRightChild(index):
            return self.items[self.getRightChildIndex(index)]
        return None

    def parent(self, index):
        index = self.getParentIndex(index)
        if index != None:
            return self.items[index]
        return None

    def swap(self, indexOne, indexTwo):
        self.items[indexOne], self.items[indexTwo] = self.items[
            indexTwo], self.items[indexOne]
        pass

    def peek(self):
        if (self.size == 0): return None
        return self.items[0]

    def poll(self):
        if (self.size == 0): return None
        item = self.items[0]
        self.items[0] = self.items[self.size - 1]
        self.size -= 1
        self.heapifyDown()
        return item

    def add(self, item):
        if (len(self.items) > self.size):
            self.items[self.size] = item
        else:
            self.items.append(item)
        self.size += 1
        self.heapifyUp()
        pass

    def heapifyDown(self):
        index = 0
        while (index < self.size - 1):
            minChild = None
            minIndex = None
            if self.hasLeftChild(index):
                minChild = self.leftChild(index)
                minIndex = self.getLeftChildIndex(index)
            if self.hasRightChild(index):
                rightChild = self.rightChild(index)
                if rightChild < minChild:
                    minChild = rightChild
                    minIndex = self.getRightChildIndex(index)
            if minChild == None:
                break
            if (self.items[index] > minChild):
                self.swap(index, minIndex)
                index = minIndex
            else:
                break

    def heapifyUp(self):
        index = self.size - 1
        while (index > 0):
            parentIdx = self.getParentIndex(index)
            if self.items[parentIdx] > self.items[index]:
                self.swap(index, parentIdx)
                index = parentIdx
            else:
                break
        pass


heap = MinInHeap()
print(heap.getLeftChildIndex(2))
print(heap.getRightChildIndex(2))
print(heap.getParentIndex(1))
print(heap.getParentIndex(2))

print(heap.hasLeftChild(2))
print(heap.hasLeftChild(3))

print(heap.leftChild(2))
print(heap.rightChild(3))

print(heap.parent(2))
print(heap.parent(3))

print(heap.hasParent(0))

print(heap.items, heap.size)
print(heap.add(3))
print(heap.items, heap.size)

print(heap.poll())
print(heap.items, heap.size)

class Heap(object):
    def __init__(self, comparator_func):
        self.heap = []
        self.size = 0
        self.compare = comparator_func

    def bubbleDown(self, idx):
        if 2*idx + 1 >= self.size:
            return

        if self.compare(self.heap[2*idx+1], self.heap[idx]) == -1:
            self.swap(idx, idx*2+1)
            self.bubbleDown(idx*2+1)
            return

    def swap(self, x, y):
        self.heap[x], self.heap[y] = self.heap[y], self.heap[x]

    def bubbleUp(self, idx):
        parent_idx = idx//2
        if parent_idx < 0:
            return

        if self.compare(self.heap[parent_idx], self.heap[idx]) == -1:
            self.swap(idx, parent_idx)
            self.bubbleUp(parent_idx)
            return

    def add(self, val):
        if not self.heap:
            self.heap = [val]
            self.size = 1
        else:
            self.heap.append(val)
            self.size += 1
            self.bubbleUp(self.size-1)

    def removePriority(self):
        min = self.heap.pop(0)
        self.heap[0] = self.heap[self.size-1]
        self.size -= 1
        self.bubbleDown(0)
        return min

    def getPriority(self):
        return self.heap[0]

    def printHeap(self):
        """
            Print something like
                        root

        """
        start_expo = 0
        while  <

    def __str__(self):
        return "Heap with size {}"


def heap_sort(arr):
    pass

class MaxHeap:
    def __init__(self) -> None:
        self.heap = []

    def push(self, val: int) -> None:
        self.heap.append(val)
        self.shift_up()

    def pop(self) -> int:
        ret = self.heap.pop(0)
        if len(self.heap) > 0:
            self.shift_down()
        return ret

    def heapify(self, iterable) -> None:
        self.heap = iterable
        self.shift_down()

    def shift_up(self):
        index = len(self.heap) - 1
        while index > 0:
            parent = index - 1
            if self.heap[parent] > self.heap[index]:
                return None
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent

    def shift_down(self) -> None:
        l = len(self.heap)
        for i in range(l):
            for i in range(l):
                left = 2*i + 1
                right = 2*i + 2
                maximum = i
                if right < l and self.heap[right] >= self.heap[i]:
                    maximum = right
                if left < l and self.heap[left] >= self.heap[maximum]:
                    maximum = left
                if maximum != i:
                    self.heap[i], self.heap[maximum] = self.heap[maximum], self.heap[i]

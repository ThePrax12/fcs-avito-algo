class Minheap:
    def __init__(self):
        self.heap = []

    def __len__(self):
        return len(self.heap)

    def _sift_down(self, idx):
        n = len(self.heap)
        while True:
            left = 2 * idx + 1
            right = 2 * idx + 2
            idx_min = idx

            if left < n and self.heap[left] < self.heap[idx_min]:
                idx_min = left
            if right < n and self.heap[right] < self.heap[idx_min]:
                idx_min = right

            if idx_min == idx:
                break

            self.heap[idx], self.heap[idx_min] = self.heap[idx_min], self.heap[idx]
            idx = idx_min

    def _sift_up(self, idx):
        while idx > 0:
            parent = (idx - 1) // 2
            if self.heap[idx] < self.heap[parent]:
                self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
                idx = parent
            else:
                break

    def push(self, value):
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)

    def pop_min(self):
        n = len(self.heap)
        result = self.heap[0]
        last = self.heap.pop()

        if n > 1:
            self.heap[0] = last
            self._sift_down(0)

        return result

    def min_el(self):
        return self.heap[0]

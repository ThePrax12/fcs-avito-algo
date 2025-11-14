from Minheap import Minheap
import heapq


def kth_largest_without_heapq(arr, k):
    heap = Minheap()
    for el in arr:
        if len(heap) < k:
            heap.push(el)
        else:
            if el > heap.min_el():
                heap.pop_min()
                heap.push(el)

    return heap.min_el()


def kth_largest_with_heapq(arr, k):
    heap = []
    for el in arr:
        if len(heap) < k:
            heapq.heappush(heap, el)
        else:
            if el > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, el)

    return heap[0]

def makeheap_n_log_n(arr):
    """
    Простой makehaep. Идём в цикле за n. Каждый шаг поднимаем элемент к вершине дерева за log(n).
    Итого n*log(n)
    """
    heap = []
    for idx, el in enumerate(arr):
        heap.append(el)
        parent_idx = (idx - 1) // 2
        while idx > 0 and heap[parent_idx] > heap[idx]:
            heap[parent_idx], heap[idx] = heap[idx], heap[parent_idx]
            idx, parent_idx = parent_idx, (parent_idx - 1) // 2

    return heap


def sift_down(arr, idx, n):
    while True:
        left = 2 * idx + 1
        right = 2 * idx + 2
        idx_min = idx

        if left < n and arr[left] < arr[idx_min]:
            idx_min = left
        if right < n and arr[right] < arr[idx_min]:
            idx_min = right

        if idx_min == idx:
            break

        arr[idx], arr[idx_min] = arr[idx_min], arr[idx]
        idx = idx_min


def makeheap(arr):
    """
    Более сложный алгоритм перестроения куч, доказательство на фото.
    Итого n
    """
    n = len(arr)
    last_parent = (n - 2) // 2

    for idx in range(last_parent, -1, -1):
        sift_down(arr, idx, n)
    return arr

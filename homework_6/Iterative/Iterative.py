def partition(nums, low, high):
    mid = nums[(low + high) // 2]
    i, j = low, high
    while i <= j:
        while nums[i] < mid:
            i += 1
        while nums[j] > mid:
            j -= 1
        if i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    return i


def quicksort_iter(nums):
    stack = [(0, len(nums) - 1)]
    while stack:
        low, high = stack.pop()
        if low >= high:
            continue
        p = partition(nums, low, high)
        stack.append((low, p - 1))
        stack.append((p, high))
    return nums


def merge(left, right):
    i = j = 0
    out = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i])
            i += 1
        else:
            out.append(right[j])
            j += 1
    out.extend(left[i:])
    out.extend(right[j:])

    return out


def mergesort_iter(nums):
    step = 1
    while step < len(nums):
        out = []
        for i in range(0, len(nums), 2 * step):

            out += merge(nums[i : i + step], nums[i + step : i + 2 * step])
        nums = out
        step *= 2

    return nums

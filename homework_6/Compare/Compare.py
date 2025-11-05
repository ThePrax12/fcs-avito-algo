import time


def time_spend(func):
    func._is_active = False

    def wrapper(*args, **kwargs):
        if func._is_active == False:
            func._is_active = True
            t1 = time.time()
            ans = func(*args, **kwargs)
            t2 = time.time()
            print("time spent:", t2 - t1)
            func._is_active = False
            return ans

        return func(*args, **kwargs)

    return wrapper


@time_spend
def quicksort_recur(nums):
    if len(nums) <= 1:
        return nums
    mid = nums[(len(nums) - 1) // 2]
    left = [x for x in nums if x < mid]
    equal = [x for x in nums if x == mid]
    right = [x for x in nums if x > mid]
    return quicksort_recur(left) + equal + quicksort_recur(right)


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

    out += left[i:] + right[j:]

    return out


def mergesort_recur(nums):
    if len(nums) <= 1:
        return nums
    mid_idx = len(nums) // 2
    left = mergesort_recur(nums[:mid_idx])
    right = mergesort_recur(nums[mid_idx:])
    return merge(left, right)

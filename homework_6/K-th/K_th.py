def quick_select(nums, k):
    if k == 0:
        return nums[0]

    p = nums[len(nums) // 2]
    greater = [x for x in nums if x > p]
    equal = [x for x in nums if x == p]
    less = [x for x in nums if x < p]

    if k <= len(greater):
        return quick_select(greater, k)
    elif k <= len(greater) + len(equal):
        return p
    else:
        return quick_select(less, k - len(greater) - len(equal))

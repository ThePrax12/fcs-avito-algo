def solition(nums: str) -> int:
    """
    Считает максимальную чётную сумму элементов массива

    Аргументы:
        nums (str): Целые положительные числа через пробел (строкой)

    Возвращает:
        int: Максимальная чётная сумма.
    """
    nums_arr = list(map(int, nums.split()))
    odd_cnt = 0
    min_odd = float("inf")
    sm = 0

    for num in nums_arr:
        sm += num
        if num % 2 == 1:
            odd_cnt += 1
            min_odd = min(min_odd, num)

    if odd_cnt % 2 == 1:
        return sm - min_odd
    return sm

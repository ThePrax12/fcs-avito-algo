def solition(num: int) -> bool:
    """
    Проверяет, является ли целое положительное число палиндромом.

    Аргументы:
        num (int): Проверяемое целое положительное число.

    Возвращает:
        bool: True если число читается одинаково слева направо и справа налево, иначе False.
    """
    if num < 0:
        return False
    num_arr = []
    n = 0
    while num:
        num_arr.append(num % 10)
        num //= 10
        n += 1

    for i in range(n // 2):
        if num_arr[i] != num_arr[n - i - 1]:
            return False
    return True

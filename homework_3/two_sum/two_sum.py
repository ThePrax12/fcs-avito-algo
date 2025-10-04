def solution(arr, k):
    """
    Находит индексы двух элементов массива, сумма которых равна k.
    Работает через хеш-таблицу и поиск по предыдущим значениям в ней.

    Параметры:
        arr (list[int]): массив чисел
        k int: исходное число

    Возвращает:
        tuple(int): два индекса, идущих по порядку.
    """
    val_dict = {}
    for i, e in enumerate(arr):
        if k - e in val_dict:
            return val_dict[k - e], i
        val_dict[e] = i

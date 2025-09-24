def solition(N: int) -> int:
    """
    Считает количество простых чисел < N с помощью решета Эратосфена

    Аргументы:
        N (int): Число, меньше которого нужно искать простые числа

    Возвращает:
        int: Количество простых чисел
    """
    if N < 2:
        return 0
    dropped_cnt = 1
    visited = set()
    for i in range(2, int(N**0.5) + 1):
        for j in range(i * i, N, i):
            if j not in visited:
                visited.add(j)
                dropped_cnt += 1

    return N - 1 - dropped_cnt

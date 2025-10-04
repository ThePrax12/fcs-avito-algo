from collections import defaultdict


def solution(strs):
    """
    Группирует слова по анаграммам.

    Каждое слово представляется в виде вектора длиной 26,
    где каждая позиция соответствует количеству конкретной буквы ('a'–'z').
    Все слова с одинаковым вектором считаются анаграммами
    и помещаются в одну группу.

    Параметры:
        strs (list[str]): Список слов, состоящих из латинских букв.

    Возвращает:
        list[list[str]]: Список групп анаграмм.
        В каждой подгруппе — слова, являющиеся анаграммами друг друга.
    """
    word_dict = defaultdict(set)
    for word in strs:
        key = [0] * 26
        for ch in word.lower():
            key[ord(ch) - ord("a")] += 1
        key = tuple(key)
        word_dict[key].add(word)
    return [list(arr) for arr in word_dict.values()]
